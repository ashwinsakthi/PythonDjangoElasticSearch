from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Document, Text, Date, Search
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

connections.create_connection()


class BlogPostIndex(Document):
    class Index:
        index = 'blogpost-index'
        name = 'blogpost-index'

    author = Text()
    posted_date = Date()
    title = Text()
    text = Text()


# Bulk indexing function, run in shell
def bulk_indexing():
    BlogPostIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.BlogPost.objects.all().iterator()))


# Simple search function
def search(author):
    s = Search().filter('term', author=author)
    response = s.execute()
    return response
