from django.db import models
from django.db.models.signals import post_delete

from transcodeandstream.settings import TAS_VIDEOS_DIRECTORY


class EncodeQueueEntryManager(models.Manager):

    def get_new_entries(self):
        return super(EncodeQueueEntryManager, self).exclude(working_on=True)


class EncodeQueueEntry(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True)
    original_filename = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    working_on = models.BooleanField(default=False)
    progress = models.PositiveSmallIntegerField(default=0)
    error = models.BooleanField(default=False)
    log = models.TextField(null=True)

    objects = EncodeQueueEntryManager()

    class Meta:
        ordering = ('created_at',)


class VirtualFilesystemNodeManager(models.Manager):

    def node_by_path(self, path):
        if not path:
            return None

        components = path.split('/')
        last_node = None
        for component in components:
            node = super(
                VirtualFilesystemNodeManager,
                self).get(parent=last_node,
                          name=component)
            last_node = node
        return last_node


class VirtualFilesystemNode(models.Model):
    name = models.CharField(max_length=255)
    video = models.CharField(max_length=10, null=True)
    parent = models.ForeignKey('self', related_name='children', null=True)

    objects = VirtualFilesystemNodeManager()

    def is_dir(self):
        return self.video is None

    def filename(self):
        if self.video:
            return os.path.join(TAS_VIDEOS_DIRECTORY, instance.name + '.webm')
        return None

    def path(self):
        node = self
        components = []
        while node:
            components.prepend(node.name)
            node = node.parent
        return '/'.join(components)

    class Meta:
        ordering = ('video', 'name')
        unique_together = ('name', 'parent')


def delete_physical_file(sender, **kwargs):
    instance = kwargs.get('instance')
    assert(instance)
    filename = instance.filename()

    if filename and os.path.exists(filename):
        os.unlink(filename)

post_delete.connect(delete_physical_file, sender=VirtualFilesystemNode)
