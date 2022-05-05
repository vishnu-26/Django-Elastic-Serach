from rest_framework import serializers

from .models import Category,Article
from user.models import User
from user.serializers import UserSerializer
from .documents import ArticleDocument


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, required=False)
    author = UserSerializer()

    def create(self, data):
        print("HII")
        categories = data.pop('categories')
        author_id = data.pop('author_id')

        author = User.objects.get(pk= user_id)
        data['author'] = author
        article  = Article.objects.create(**data)

        for _category in categories:
            article.categories.add(_category)

        return article

    class Meta:
        model= Article
        fields='__all__'


# class ArticleDocumentSerializer(DocumentSerializer):
# 
#     class Meta:
#         document = ArticleDocument
#         fields = '__all__'
