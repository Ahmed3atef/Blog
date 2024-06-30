from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .serializers import CommentSerializer
from .models import Post,Comment
from .forms import PostForm

class Index(ListView):
    model=Post
    template_name="blog/index.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class BlogCreateView(LoginRequiredMixin,CreateView):
    model=Post
    template_name='blog/post_new.html'
    form_class = PostForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 
    enctype = "multipart/form-data"

class BlogUpateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    template_name = "blog/post_edit.html"
    form_class = PostForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self): 
        obj = self.get_object()
        return obj.author == self.request.user
    enctype = "multipart/form-data"

class BlogDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    template_name="blog/post_delete.html"
    success_url=reverse_lazy('index')
    def test_func(self): 
        obj = self.get_object()
        return obj.author == self.request.user

class PostCreateCommentView(LoginRequiredMixin,generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    

class PostDeleteCommentView(LoginRequiredMixin,generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer