from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy

from webapp.models import Poll, Choice
from webapp.forms import PollForm, ChoiceForm, SimpleSearchForm
from django.views.generic import View, DetailView, CreateView
from webapp.views import SearchView, EditView, DeleteView


class IndexViews(SearchView):
    template_name = 'choice/index.html'
    context_object_name = 'choices'
    model = Choice
    # ordering = ('-updated_at',)
    paginate_by = 10
    paginate_orphans = 2
    search_form_class = SimpleSearchForm
    search_fields = ['summary__icontains', 'description__icontains']

    def post(self, request, *args, **kwargs):
        for task_pk in request.POST.getlist('tasks', []):
            self.model.objects.get(pk=task_pk).delete()
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


# class TaskView(DetailView):
#     template_name = 'task/task_view.html'
#     model = Tracker
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['task'] = get_object_or_404(Tracker, pk=self.kwargs.get('pk'))
#         return context

class ChoiceCreate(CreateView):
    template_name = 'choice/create.html'
    model = Choice
    form_class = ChoiceForm

class ChoiceEdit(EditView):
    form_class = ChoiceForm
    template_name = 'choice/choice_edit.html'
    model = Choice
    task = None
    context_object_name = 'choices'
    redirect_url = 'index'


class TaskDelete(DeleteView):
    template_name = 'choice/choice_delete.html'
    model = Choice
    context_key = 'choise'
    redirect_url = reverse_lazy('index')