from django.urls import path
# from . import views
from .views import BlogView, BlogDetailView, AddPostView


urlpatterns = [
    # path('', views.BlogView, name='blogs-view'),
    path('', BlogView.as_view(), name="blog-view"),
    path('blogs/<int:pk>', BlogDetailView.as_view(), name='blog-detail'),
    path('add_post/', AddPostView.as_view(), name='add-post'),
]
