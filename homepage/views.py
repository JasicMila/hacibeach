from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Page, Image
from django.utils import translation
from django.conf import settings
from django.utils.translation import get_language
from .forms import ImageForm



def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')


def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    language_code = translation.get_language_from_request(request, check_path=True)
    page_contents = page.pagecontent_set.all()

    # Now let's find the appropriate translations
    for content in page_contents:
        if language_code == 'tr':  # Turkish text is not stored as a translation
            content.translated_text = content.text
        else:
            translated_content = content.translations.filter(language=language_code).first()
            if translated_content:
                content.translated_text = translated_content.translated_text
            else:
                # If there is no translation in the chosen language, load the Turkish version
                content.translated_text = content.text

    context = {
        'page': page,
        'page_contents': page_contents,
        'language_code': language_code,
    }
    return render(request, 'page_detail.html', context)


def gallery(request):
    images = Image.objects.all()
    return render(request, 'gallery.html', {'images': images})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})
