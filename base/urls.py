

from base.models import Task
from django.urls import path
from django.views.generic.base import View
from .views import TaskDelete, TaskList,TaskDetail,TaskCreate, TaskUpadte



urlpatterns = [
    path('', TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(),name='detail'),
    
    path('create/', TaskCreate.as_view(),name='create'),
    path('task-update/<int:pk>/', TaskUpadte.as_view(),name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(),name='task-delete'),

]
