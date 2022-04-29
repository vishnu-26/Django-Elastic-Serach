from django.urls import path, include
from .views import create_article, articles

urlpatterns = [
    path('create', create_article),
    path('', articles)
]