from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import CreatePost, UpdatePost, AddComment
from django.urls import reverse_lazy, reverse


class BlogView(ListView):
    model = Post
    template_name = 'blog/blog_view.html'
    ordering = ['-id']


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = CreatePost
    template_name = 'blog/add_post.html'


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePost
    template_name = 'blog/update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog-view')


class AddCommentView(CreateView):
    model = Comment
    form_class = AddComment
    template_name = 'blog/add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        post_id = self.kwargs['pk']
        return reverse('blog-detail', kwargs={'pk': post_id})
