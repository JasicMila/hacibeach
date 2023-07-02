from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Page, Image, ContactRequest, PageContent
from django.utils import translation
from django.conf import settings
from django.utils.translation import get_language
from .forms import ImageForm, ContactForm
import logging
from django.contrib import messages


def home(request):
    language_code = translation.get_language_from_request(request, check_path=True)
    about = Page.objects.get(slug='about')
    about_page_content = set_single_translation(about.pagecontent_set.first(), language_code)
    
    beach = Page.objects.get(slug='beach')
    beach_page_content = set_translations(beach.pagecontent_set.filter(), language_code)
    
    restaurant = Page.objects.get(slug='restaurant')
    restaurant_page_content = set_translations(restaurant.pagecontent_set.filter(), language_code)
    
    stay = Page.objects.get(slug='stay')
    stay_page_content = set_translations(stay.pagecontent_set.filter(), language_code)
    
#     logger = logging.getLogger(__name__)
#     logger.debug(stay.id)
    
    context = {
        'about_page_content': about_page_content,
        'beach_page_content': beach_page_content,
        'restaurant_page_content': restaurant_page_content,
        'stay_page_content': stay_page_content,
        'language_code': language_code,
        'form': None
    }
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            # Create a new ContactRequest instance with the form data
            contact_request = ContactRequest(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            contact_request.save()  # Save the instance to the database
            
            messages.success(request, 'Your contact request has been submitted.')
        else:
            context['form'] = form
            
            return render(request, 'home.html', context)
            
        return redirect(f'/{language_code}/#contact')  # Redirect to a success page
    else:
        context['form'] = ContactForm()
        
    return render(request, 'home.html', context)


def set_translations(content, language_code):
    for data in content:
        data = set_single_translation(data, language_code)
    
    return content    
    
def set_single_translation(content, language_code):
    # Now let's find the appropriate translations
    if language_code == 'tr':  # Turkish text is not stored as a translation
        content.translated_text = content.text
    else:
        translated_content = content.translations.filter(language=language_code).first()
        if translated_content:
            content.translated_text = translated_content.translated_text
        else:
            # If there is no translation in the chosen language, load the Turkish version
            content.translated_text = content.text
    
    return content

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
