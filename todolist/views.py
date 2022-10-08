from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest
from .models import Todolist

# Create your views here.

def todo_list_items(request):
    context = {'task_list' : Todolist.objects.all()}
    return render(request, 'todolist/todo.html',context)

def insert_todolist(request:HttpRequest):
    todolist = Todolist(content = request.POST['content'])
    todolist.save()
    return redirect('/todolist/list/')

def delete_list_items(request,todolist_id):
    todo_to_delete = Todolist.objects.get(id=todolist_id)
    todo_to_delete.delete()
    return redirect('/todolist/list/')
