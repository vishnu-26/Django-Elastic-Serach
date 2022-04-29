from django.shortcuts import render
from .models import User

from rest_framework.decorators import api_view
from django.http import JsonResponse

# Create your views here.

@api_view(['POST'])
def register(request):
    pass

    


