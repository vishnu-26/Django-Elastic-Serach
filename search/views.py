from elasticsearch_dsl import Q
from rest_framework.decorators import api_view
from django.http import JsonResponse

from article.serializers import CategorySerializer, ArticleSerializer
from article.documents import ArticleDocument
# from article.serializers import ArticleDocumentSerializer


@api_view(['GET'])
def search_article(request):
    print(request.query_params)
    query = request.query_params.get('search',None)

    q = Q(
        'multi_match',
        query= query,
        fields= [
            'title',
            'categories',
            'author',
            'content'
        ],
        fuzziness= 'auto'
    )

    search = ArticleDocument.search().query(q)
    response = search.execute()
    print(response)

    articles = ArticleSerializer(response, many=True).data
    # print(articles)

    return JsonResponse({
        'articles': articles
    },status=201)
