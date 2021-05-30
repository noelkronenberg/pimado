from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem
import os
import mimetypes
from django.http.response import HttpResponse

def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html', 
    {'all_items': all_todo_items})

def addTodo(request):
    new_item = TodoItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')

def dashboardView(request):
    context = {}
    all_todo_items = TodoItem.objects.all()
    all_todo_items_list = []
    for i in all_todo_items:
        singular_item = i.content
        all_todo_items_list.append(singular_item)
    markdown_list_cache = []
    for i in all_todo_items_list:
        item = '- [ ] ' + i
        markdown_list_cache.append(item)
    markdown_list = '\n'.join(markdown_list_cache)
    with open('to-do-list.md', 'w') as f:
        f.write(markdown_list)
    return render(request, 'dashboard.html', context)

def download_file(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'to-do-list.md'
    filepath = BASE_DIR + '/' + filename
    path = open(filepath, 'r')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
