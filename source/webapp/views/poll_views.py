from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy

from webapp.models import Poll, Choice
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from webapp.forms import PollForm
from webapp.views import EditView


class PollListView(ListView):
    template_name = 'poll/index.html'
    model = Poll
    context_object_name = 'polls'
    paginate_by = 4
    # paginate_orphans = 2
    ordering = '-created_at'

class PollDetail(DetailView):
    model = Poll
    template_name = 'poll/poll_view.html'


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
    def get_success_url(self):
        return reverse('index')
