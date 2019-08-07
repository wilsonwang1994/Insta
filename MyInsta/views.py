from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from MyInsta.forms import CustomUserCreationForm

# Create your views here.

class HelloDjango(TemplateView):
    template_name = 'home.html'

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'home.html'
    login_url = "login"

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
 
class PostCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = '__all__'

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title']
    template_name = 'post_edit.html'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
