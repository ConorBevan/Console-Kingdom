from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


# def BlogView(request):
#    return render(request, 'blog/blog_view.html', {})

class BlogView(ListView):
    model = Post
    template_name = 'blog/blog_view.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_details.html'


class AddPostView(CreateView):
    model = Post
    template_name = 'blog/add_post.html'
    fields = ('title', 'content')
