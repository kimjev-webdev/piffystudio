from django.urls import path
from . import views

urlpatterns = [
    path('installations/', views.installations, name='work_installations'),
    path('digital/', views.digital, name='work_digital'),
    path('art/', views.art, name='work_art'),
]
