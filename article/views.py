from rest_framework import serializers
from rest_framework.decorators import api_view
from django.http import JsonResponse

from .serializers import CategorySerializer,ArticleSerializer
from .models import Category,Article
from user.models import User

# Create your views here.

@api_view(['POST'])
def create_article(request):
    data = request.data

    # serializer = ArticleSerializer(data= request.data)
    # if serializer.is_valid():
    #     serializer.save()
    # else:
    #     print("Invalid Data!!")
    #
    # article = serializer.data


    author = User.objects.get(pk= data['author'])
    article = Article.objects.create(
        title = data['title'],
        content = data['content'],
        author = author
    )

    article.save()

    for category in data['categories']:
        _category,created = Category.objects.get_or_create(name= category)
        print(_category.__dict__)
        article.categories.add(_category)

    article = ArticleSerializer(article).data

    return JsonResponse(
        {'article': article},status= 201
    )

@api_view(['GET'])
def articles(request):

    # article = Article.objects.get(title='How to improve your Google rating?')
    # categories = list(article.categories.all().values())

    # article.__dict__.pop('_state')
    # article['categories'] = categories
    # print(article)

    # # for article in articles

    articles = ArticleSerializer(Article.objects.all(),many=True).data

    return JsonResponse({
        'articles': articles},status= 200
    )
