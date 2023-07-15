from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's no items in your cart!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NU8UqLeBDUOjXVrLfNDNbjVQa5qovPNi0m6giq18VW9vB2jiAtoGFwTvF6He0uBXf01CRsIoBDLxnrQ49JumZbr00Efs25iw1',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
