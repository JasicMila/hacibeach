from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Page, Image

# Create your views here.
def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'page_detail.html', {'page': page})

def gallery(request):
    images = Image.objects.all()
    return render(request, 'gallery.html', {'images': images})