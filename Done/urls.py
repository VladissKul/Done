"""Done URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from todo import views
from rest_framework import routers
from todo.views import TodoViewSet
from notes.views import *

todo_router = routers.SimpleRouter()
todo_router.register(r'all_todos', TodoViewSet)

urlpatterns = [
    # API
    path('api/', include(todo_router.urls)),
    # Healthcheck
    path('healthcheck', views.healthcheck, name='healthcheck'),
    # Admin
    path('admin/', admin.site.urls),
    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),
    # Todos
    path('create_todo/', views.create_todo, name='create_todo'),
    path('current_todos/', views.current_todos, name='current_todos'),
    path('completed_todos/', views.completed_todos, name='completed_todos'),
    path('todo/<int:todo_pk>', views.viewtodo, name='viewtodo'),
    path('todo/<int:todo_pk>/complete', views.completetodo, name='completetodo'),
    path('todo/<int:todo_pk>/delete', views.deletetodo, name='deletetodo'),
    path('', views.home, name='home'),
    # Notes
    path('create_note', create_note, name='create_note'),
    path('notes_list/', notes_list, name='notes_list'),
    path('notes_list/<int:note_id>', note_detail, name='note_detail'),
    path('notes_list/<int:note_id>/delete', delete_note, name='delete_note'),

]


