from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import FormPost, FormEdit
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']
    
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'articles_detail.html'
    
class AddPostView(CreateView):
    model = Post
    # form_class = FormPost
    template_name = 'add_post.html'
    fields = ('title','author','body')
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = FormEdit
    template_name = 'update_post.html'
    # fields = '__all__'
    
    
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')