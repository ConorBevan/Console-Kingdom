from django.shortcuts import render
from .models import Contact


def contact_view(request):
    return render(request, 'contacts/contact_page.html')
