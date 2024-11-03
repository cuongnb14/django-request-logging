Django Request Logging
===================

Install
=======

::

    pip install git+https://github.com/cuongnb14/django-request-logging.git@v1.2#egg=django-request-logging

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
        'WHITELIST_PATHS': ["/admin/jsi18n/"],
        'ENABLE_PYTHON_LOG': True,
        'ENABLE_DB_LOG': True,
        'DB_LOG_SAMPLE': 1,
        'LOG_HEADER_KEYS': ["HTTP_USER_AGENT", "HTTP_X_FORWARDED_FOR", "REMOTE_ADDR", "HTTP_REFERER"],
    }


Run migrate:

::

    python3 manage.py migrate
