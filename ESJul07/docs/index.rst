.. Elasticsearch for Django REST Framework documentation master file, created by
   sphinx-quickstart on Tue Apr 18 18:54:08 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Elasticsearch for Django REST Framework's
=========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   basic-usage
   pagination
   ordering

About
-----
Django REST Elasticsearch provides the easy way for integration `Django REST Framework <http://django-rest-framework.org/>`_ and `Elasticsearch <https://github.com/elastic/elasticsearch>`_.
The library uses `Elasticsearch DSL <https://github.com/elastic/elasticsearch-dsl-py>`_ library, it is a high-level library to the official low-level client.

Requirements
------------
- Django REST Framework 3.5 and above
- elasticsearch-dsl>=5.0.0,<7.0.0 (*Elasticsearch 5.x*)

Installation
------------
.. code-block:: none

    pip install django-rest-elasticsearch

Changelog
---------

v0.4
......

*Release date: 2018-03-03*
    - Add tests

v0.3.4
......

*Release date: 2018-01-20*
    - Fixed small bugs

v0.3.3
......

*Release date: 2017-11-30*
    - Added a support of the API schema
    - Remove None values from gte/lte range filter

v0.3.2
......

*Release date: 2017-09-06*
    - Fixed the bug with the paginator class
    - Remove Django<1.11 from the requirement

v0.3.0
......

*Release date: 2017-06-26*
    - Fixed the bug with filtering by boolean values
    - Added validation

v0.2.0
......

*Release date: 2017-04-07*
    - Initial release.
