from django.urls import path

from .views import search_article

urlpatterns = [

    path('article/', search_article)
]
