from django.contrib import admin
from django.urls import path
from webapp.views import PollListView, PollDetail, PollEdit, PollCreate, PollDelete
from webapp.views.choice_views import ChoiceCreate, ChoiceEdit, ChoiceDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PollListView.as_view(), name='index'),
    path('poll/<int:pk>/', PollDetail.as_view(), name='poll_view'),
    path('poll/add/', PollCreate.as_view(), name='poll_add'),
    path('poll/<int:pk>/edit/', PollEdit.as_view(), name='poll_edit'),
    path('poll/<int:pk>/delete/', PollDelete.as_view(), name='poll_delete'),
    path('choice/<int:pk>/add', ChoiceCreate.as_view(), name='choice_add'),
    path('choice/<int:pk>/edit', ChoiceEdit.as_view(), name='choice_edit'),
    path('choice/<int:pk>/delete/', ChoiceDelete.as_view(), name='choice_delete'),
]
