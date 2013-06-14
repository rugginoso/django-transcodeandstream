from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, Http404
from django.template.context import RequestContext
import json

from transcodeandstream.models import VirtualFilesystemNode, EncodeQueueEntry
from transcodeandstream import forms


def queue(request):
    return render_to_response('transcodeandstream/queue.html')


def queue_data(request):
    entries = EncodeQueueEntry.objects.values(
        'original_filename',
        'transcode_format',
        'progress',
        'error',
        'pk',
    )

    return HttpResponse(json.dumps(list(entries)), mimetype='text/json')

def queue_log(request, video_id):
    entry = get_object_or_404(EncodeQueueEntry, pk=video_id)
    return HttpResponse("<pre>%s</pre>" % entry.log)

def get_node_by_path_or_404(path):
    try:
        node = VirtualFilesystemNode.objects.node_by_path(path)
    except VirtualFilesystemNode.DoesNotExist:
        raise Http404()
    return node


def filesystem_operation(request, path=''):
    action = request.GET.get('action', 'change_directory')
    # if not action in ('create_directory, change_directory', 'show_video', 'move', 'rename', 'remove'):
    #    return HttpResponse(status=400)
    node = get_node_by_path_or_404(path)
    return globals()[action](request, node)


def create_directory(request, parent_node):
    if request.method == 'POST':
        form = forms.RenameForm(request.POST)
        if form.is_valid():
            node = VirtualFilesystemNode(name=form.cleaned_data['name'])
            node.parent = parent_node
            node.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)


def change_directory(request, node):
    if node is None or node.is_dir():
        children = list(node.children.all() if node else VirtualFilesystemNode.objects.filter(parent=None))
        context = {
            'children': sorted(children, key=lambda n: (not n.is_dir(), n.name)),
            'parent': node.parent if node else None,
            'current_path': node.path if node else None,
        }
        return render_to_response('transcodeandstream/show_directory.html', context_instance=RequestContext(request, context))
    else:
        return HttpResponse(status=400)


def show_video(request, node):
    if node is None or node.is_dir():
        return HttpResponse(status=400)
    else:
        context = {'video': node}
        return render_to_response('transcodeandstream/show_video.html', context_instance=RequestContext(request, context))


def move(request, node):
    if request.method == 'POST':
        form = forms.MoveForm(request.POST)
        if form.is_valid():
            dest_node = get_node_by_path_or_404(form.cleaned_data['path'])

            if dest_node is not None and not dest_node.is_dir():
                return HttpResponse('destination is not a direcroy', status=400)

            if dest_node and node.path == dest_node.path:
                return HttpResponse('cannot move a directory into itself', status=400)

            node.parent = dest_node
            node.save()

            return HttpResponse(status=200)

        else:
            return HttpResponse(status=400)

def rename(request, node):
    if request.method == 'POST':
        form = forms.RenameForm(request.POST)
        if form.is_valid():
            node.name = form.cleaned_data['name']
            node.save()
            return HttpResponse(status=200)


def remove(request, node):
    if request.method == 'POST':
        form = forms.DeleteForm(request.POST)
        if form.is_valid():
            node.delete()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)
