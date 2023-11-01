from django.urls import path
from .views import BlogView, BlogDetailView, AddPostView, UpdatePostView, DeletePostView, AddCommentView


urlpatterns = [
    path('', BlogView.as_view(), name="blog-view"),
    path('blogs/<int:pk>', BlogDetailView.as_view(), name='blog-detail'),
    path('add_post/', AddPostView.as_view(), name='add-post'),
    path('blogs/update/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('blogs/<int:pk>/delete', DeletePostView.as_view(), name='delete-post'),
    path('blogs/<int:pk>/comment', AddCommentView.as_view(), name='add-comment'),
]
