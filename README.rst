Django Request Logging
===================

Install
=======

::

    pip install git+https://github.com/cuongnb14/django-request-logging.git@v1.1#egg=django-request-logging

Setting
=======

.. code:: python

    INSTALLED_APPS = [
        'request_logging',
        ...
    ]

    MIDDLEWARE = [
        ...
        'request_logging.middlewares.RequestLogMiddleware'
    ]

    REQUEST_LOGGING = {
        'WHITELIST_PATHS': [],
        'ENABLE_PYTHON_LOG': True,
        'ENABLE_DB_LOG': True,
    }


Run migrate:

::

    python3 manage.py migrate
