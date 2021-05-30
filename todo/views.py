from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem
from markdownify import markdownify
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
    all_todo_items = #content of every TodoItem
    conversion_input = all_todo_items
    conversion_output = markdownify(conversion_input)
    context['generated_md'] = conversion_output
    return render(request, 'dashboard.html', context)