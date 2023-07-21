from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order
from django.contrib.auth.decorators import login_required


@login_required
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
        'on_user_page': True  # need to follow toast steps to stop bag appearing when updating profile
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is the order number: {order_number}. '
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
