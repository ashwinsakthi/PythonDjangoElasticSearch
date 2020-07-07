.. _pagination-label:

==========
Pagination
==========

Example of the pagination response

.. code:: python

    class BlogView(es_views.ListElasticAPIView):
        es_client = Elasticsearch(hosts=['elasticsearch:9200/'],
                                  connection_class=RequestsHttpConnection)

        es_pagination_class = es_pagination.ElasticLimitOffsetPagination

        es_model = BlogIndex
        es_filter_backends = (
            es_filters.ElasticFieldsFilter,
            es_filters.ElasticSearchFilter
        )
        es_filter_fields = (
            es_filters.ESFieldFilter('tag', 'tags'),
        )
        es_search_fields = (
            'tags',
            'title',
        )
