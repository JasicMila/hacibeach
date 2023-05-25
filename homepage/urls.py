from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('page/<slug:slug>/', views.page_detail, name='page_detail'),
    path('gallery/', views.gallery, name='gallery'),

]