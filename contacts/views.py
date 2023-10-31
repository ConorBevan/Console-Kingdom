from django.shortcuts import render
from .models import Contact
from django.contrib import messages


def contact_view(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact.name=name
        contact.email=email
        contact.message=message
        contact.save()
        messages.success(request, f'Thanks for getting in touch. A memebr of our team will get in contact with you shortly!')

    return render(request, 'contacts/contact_page.html')
