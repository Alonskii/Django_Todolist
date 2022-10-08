from django.urls import path
from . import views

urlpatterns =[
    path('list/',views.todo_list_items),
    path('insert_todo/',views.insert_todolist,name='insert_list'),
    path('delete_todo/<int:todolist_id>/',views.delete_list_items,name='delete_list'),
]
