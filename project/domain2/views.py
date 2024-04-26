from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.http import request, HttpResponseRedirect
from django.shortcuts import redirect

from .models import *
from .forms import *
from .filters import *

class PostList(ListView):
    model = Post
    queryset = Post.objects.all().order_by('-creation_date')
    template_name = 'list.html'
    context_object_name = 'posts'

class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'pdetail.html'
    context_object_name = 'details'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['response_form'] = ResponseForm()
        return context

    def post(self):
        post = self.get_object()
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.post = post
            response.user_id = request.user_id
            response.save()
            return redirect('post', pk=post.pk)


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create.html'
    context_object_name = 'create'

    def form_valid(self, form):
        form.instance.user = self.request.user
        post = form.save(commit=False)
        post.save()
        return super().form_valid(form)

    def get_absolute_url(self, **kwargs):
        return reverse_lazy('post', kwargs={'pk': self.object.pk})

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'delete.html'
    context_object_name = 'delete'
    success_url = reverse_lazy('post_list')


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'update.html'
    context_object_name = 'update'

    def get_absolute_url(self, **kwargs):
        return reverse_lazy('post', kwargs={'pk': self.object.pk})

class ResponseList(ListView, LoginRequiredMixin):
    model = Response
    ordering = 'date'
    template_name = 'response_list.html'
    context_object_name = 'response_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ResponsesFilter(self.request.GET, queryset)
        return self.filterset.qs

class ResponseDetail(DetailView, LoginRequiredMixin):
    model = Response
    template_name = 'response.html'
    context_object_name = 'response'

class ResponseCreate(CreateView, LoginRequiredMixin):
    form_class = ResponseForm
    model = Response
    template_name = 'response_create.html'
    context_object_name = 'response_create'
