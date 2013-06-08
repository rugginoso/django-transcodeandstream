from django.db import models

class EncodeQueueEntryManager(models.Manager):
	def get_new_entries(self):
		return super(EncodeQueueEntryManager, self).exclude(working_on=True)

class EncodeQueueEntry(models.Model):
	id = models.CharField(max_length=10, primary_key=True, unique=True)
	original_filename = models.CharField(max_length=255, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	working_on = models.BooleanField(default=False)
	objects = EncodeQueueEntryManager()

	class Meta:
		ordering = ('created_at',)
