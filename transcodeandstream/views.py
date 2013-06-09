from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
import json

from transcodeandstream.models import VirtualFilesystemNode, EncodeQueueEntry
from transcodeandstream import forms


def encoding_infos(request):
    entries = EncodeQueueEntry.objects.values(
        'original_filename',
        'progress',
        'error',
        'log',
    )

    return HttpResponse(json.dumps(list(entries)), mimetype='text/json')


def get_node_by_path_or_404(path):
    try:
        node = VirtualFilesystemNode.objects.node_by_path(path)
    except VirtualFilesystemNode.DoesNotExist:
        raise Http404()
    return node


def filesystem_operation(request, path):
    action = request.GET.get('action', 'change_directory')
    # if not action in ('create_directory, change_directory', 'show_video', 'move', 'rename', 'remove'):
    #    return HttpResponse(status=400)
    node = get_node_by_path_or_404(path)

    return globals()[action](request, node)


def create_directory(request, parent_node):
    if request.method == 'POST':
        form = RenameForm(request.POST)
        if form.is_valid():
            node = VirtualFilesystemNode(name=form.cleaned_data['name'])
            node.parent = parent_node
            node.save()
        else:
            return HttpResponse(status=400)


def change_directory(request, node):
    if node is None or node.is_dir():
        return render_to_response('show_directory.html', {'current_dir': node})
    else:
        return HttpResponse(status=400)


def show_video(request, node):
    if node is None or node.is_dir():
        return HttpResponse(status=400)
    else:
        return render_to_response('show_video.html', {'video': node})


def move(request, dest_node):
    if request.method == 'POST':
        if dest_node is not None and not dest_node.is_dir():
            raise Http400('destination is not a direcroy')

        form = forms.MoveForm(request.POST)
        if form.is_valid():
            node = get_node_by_path_or_404(form.cleaned_data['path'])
            node.parent = dest_node
            node.save()
            return HttpResponse(status=200)


def rename(request, node):
    if request.method == 'POST':
        form = forms.RenameForm(request.POST)
        if form.is_valid():
            node.name = form.cleaned_data['name']
            node.save()
            return HttpResponse(status=200)


def remove(request, node):
    if request.method == 'DELETE':
        node.delete()
        return HttpResponse(status=200)
