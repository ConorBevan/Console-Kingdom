from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product
# Create your views here.


def view_cart(request):
    """ A view that renders the cart contents page """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['cart'] = cart
    return redirect(redirect_url)


def edit_cart_quantity(request, item_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        del cart[item_id]

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def delete_from_cart(request, item_id):

    cart = request.session.get('cart', {})

    if item_id in cart:
        del cart[item_id]

    request.session['cart'] = cart
    return HttpResponse(status=200)
