from django.shortcuts import render


def BlogView(request):
    return render(request, 'blog/blog_view.html', {})
