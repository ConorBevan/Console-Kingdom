from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm


def user(request):
    user = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated successfully')

    form = UserProfileForm(instance=user)
    orders = user.orders.all()

    template = 'users/user.html'
    context = {
        'form': form,
        'orders': orders,
        'on_user_page': True
    }

    return render(request, template, context)
