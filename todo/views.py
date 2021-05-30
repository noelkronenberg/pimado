from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem
import os

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
    conversion_input = markdown_list
    conversion_output = conversion_input
    context['generated_md'] = conversion_output
    return render(request, 'dashboard.html', context)