from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy

from webapp.models import Poll
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from webapp.forms import PollForm
from webapp.views import EditView


class PollListView(ListView):
    template_name = 'poll/index.html'
    model = Poll
    context_object_name = 'polls'
    ordering = '-created_at'

class PollDetail(DetailView):
    model = Poll
    template_name = 'poll/poll_view.html'

    # def get_context_data(self, **kwargs):
        # polls = self.object.polls.all()
        # paginator = Paginator(polls, 10)
        # page_number = self.request.GET.get('page')
        # page_obj = paginator.get_page(page_number)
        # context = super().get_context_data(**kwargs)
        # context['page_obj'] = page_obj
        # context['is_paginated'] = page_obj.has_other_pages()
        # context['polls'] = page_obj.object_list
        # return context

class PollCreate(CreateView):
    model = Poll
    template_name = 'poll/create.html'
    form_class = PollForm

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})

class PollEdit(EditView):
    model = Poll
    template_name = 'poll/poll_edit.html'
    form_class = PollForm
    context_object_name = 'poll'
    redirect_url = 'index'

    # def get_success_url(self):
    #     return reverse('project_view', kwargs={'pk': self.object.pk})

class PollDelete(DeleteView):
    template_name = 'poll/poll_delete.html'
    model = Poll
    context_key = 'poll'
    redirect_url = reverse_lazy('index')
    # model = Poll
    # def get(self, request, *args, **kwargs):
    #     return self.delete(request, *args, **kwargs)
    #
    # def get_success_url(self):
    #     return reverse('index')
