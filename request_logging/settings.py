from django.conf import settings

REQUEST_LOGGING_SETTINGS = {
    'WHITELIST_PATHS': ["/admin/jsi18n/"],
    'ENABLE_PYTHON_LOG': True,
    'ENABLE_DB_LOG': True,
    'DB_LOG_SAMPLE': 1,
    'LOG_HEADER_KEYS': ["HTTP_USER_AGENT", "HTTP_X_FORWARDED_FOR", "REMOTE_ADDR", "HTTP_REFERER"],
}


user_settings = getattr(settings, "REQUEST_LOGGING", {})

REQUEST_LOGGING_SETTINGS.update(user_settings)
