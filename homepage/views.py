from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Page, Image
from django.utils import translation

# Create your views here.
def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    page_contents = page.pagecontent_set.prefetch_related('translations').all()
    language_code = translation.get_language()
    return render(request, 'page_detail.html', {'page': page, 'page_contents': page_contents, 'language_code': language_code})

def gallery(request):
    images = Image.objects.all()
    return render(request, 'gallery.html', {'images': images})