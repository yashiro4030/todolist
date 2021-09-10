from base.models import Task
from django.db.models.base import Model
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Task


# Create your views here.

class TaskList(ListView):
   model =Task
   context_object_name = 'liste' #pour changer ' object_list' qui affiche les data dans la page HTML, par notre propre attribut

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'detail'
    template_name='base/detail.html'  #pour que django prend en compte le nom fichier html


class TaskCreate(CreateView):
    model = Task
    fields='__all__'
    success_url=reverse_lazy('create')

class TaskUpadte(UpdateView):
    model = Task
    fields='__all__'
    success_url=reverse_lazy('tasks') # pour me rediriger à la page d'accueil 'tasks' et le nom d'url taskslist



class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'liste'
    success_url=reverse_lazy('tasks')
