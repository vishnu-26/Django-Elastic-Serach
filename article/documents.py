from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from .models import Category, Article
from user.models import User

@registry.register_document
class ArticleDocument(Document):

    author = fields.ObjectField(properties={
        'user_id': fields.TextField(),
        'name': fields.TextField(),
        'email_id': fields.TextField()
    })

    categories = fields.ObjectField(properties={
        'name': fields.TextField()
    })



    class Index:
        name = 'articles'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Article
        fields = [
            'title',
            'content',
        ]
