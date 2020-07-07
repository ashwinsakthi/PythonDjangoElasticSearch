.. _ordering-label:

========
Ordering
========

Example of ordering

.. code:: python

    class BlogView(es_views.ListElasticAPIView):
        es_client = Elasticsearch(hosts=['elasticsearch:9200/'],
                                  connection_class=RequestsHttpConnection)

        es_pagination_class = es_pagination.ElasticLimitOffsetPagination

        es_filter_backends = (
            es_filters.ElasticFieldsFilter,
            es_filters.ElasticSearchFilter,
            es_filters.ElasticOrderingFilter,
        )
        es_ordering_fields = (
            "created_at",
            ("title.raw", "title")
        )
        es_filter_fields = (
            es_filters.ESFieldFilter('tag', 'tags'),
        )
        es_search_fields = (
            'tags',
            'title',
        )
