from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),           # HOME → "/"
    path('about/', views.about, name='about'),   # ABOUT → "/about/"
    path('contact/', views.contact, name='contact'),  # CONTACT → "/contact/"
]
