# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function, unicode_literals)

from elasticsearch_dsl import (
    DocType,
    Date,
    Keyword,
    Text,
    Boolean,
    Integer
)


class BlogIndex(DocType):
    """
    BlogIndex.init(using=es_client)
    """
    class Meta:
        name = 'blog'
        index = 'blog'

    pk = Integer()
    title = Text(fields={'raw': Keyword()})
    created_at = Date()
    body = Text()
    tags = Text()
    is_published = Boolean()


