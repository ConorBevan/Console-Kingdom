from django.shortcuts import render, get_object_or_404
from .models import UserProfile


def user(request):
    user = get_object_or_404(UserProfile, user=request.user)

    template = 'users/user.html'
    context = {
        'user': user,
    }

    return render(request, template, context)
