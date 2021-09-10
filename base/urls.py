

from base.models import Task
from django.urls import path
from django.views.generic.base import View
from .views import CustomLoginView, TaskDelete, TaskList,TaskDetail,TaskCreate, TaskUpadte,RegisterPage
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('login/', CustomLoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('register/', RegisterPage.as_view(),name='register'),
    path('', TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(),name='detail'),
    
    path('create/', TaskCreate.as_view(),name='create'),
    path('task-update/<int:pk>/', TaskUpadte.as_view(),name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(),name='task-delete'),

]
