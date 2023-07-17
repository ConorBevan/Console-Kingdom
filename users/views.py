from django.shortcuts import render


def user(request):

    template = 'users/user.html'
    context = {}

    return render(request, template, context)
