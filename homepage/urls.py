from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.views.i18n import set_language

urlpatterns = [
    path('', views.home, name="home"),
#     path('contact/', views.contact, name="contact"),
#     path('contact/success/', TemplateView.as_view(template_name='contact_success.html'), name='contact_success'),
    path('page/<slug:slug>/', views.page_detail, name='page_detail'),
    path('gallery/', views.gallery, name='gallery'),
    path('upload-image/', views.upload_image, name='upload-image'),
    path('set-language/', set_language, name='set_language'),
]
