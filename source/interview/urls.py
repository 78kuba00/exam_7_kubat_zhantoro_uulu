"""interview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from webapp.views import PollListView, PollDetail, PollEdit, PollCreate, PollDelete
from webapp.views.choice_views import ChoiceCreate

# IndexView, CreateTask, TaskView, UpdateTask, DeleteTask,

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PollListView.as_view(), name='index'),
    path('poll/<int:pk>/', PollDetail.as_view(), name='poll_view'),
    path('poll/add/', PollCreate.as_view(), name='poll_add'),
    path('poll/<int:pk>/edit/', PollEdit.as_view(), name='poll_edit'),
    path('poll/<int:pk>/delete/', PollDelete.as_view(), name='poll_delete'),
    # path('task/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('poll/<int:pk>/choices/add', ChoiceCreate.as_view(), name='choice_add'),
    # path('task/', IndexViews.as_view(), name='tasks_list'),
    # path('task/<int:pk>/edit/', TaskEdit.as_view(), name='task_edit'),
    # path('task/<int:pk>/delete/', TaskDelete.as_view(), name='task_delete')
]
