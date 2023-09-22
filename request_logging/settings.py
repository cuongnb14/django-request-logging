from django.conf import settings

REQUEST_LOGGING_SETTINGS = {
    'WHITELIST_PATHS': [],
    'ENABLE_PYTHON_LOG': True,
    'ENABLE_DB_LOG': True,
}


user_settings = getattr(settings, "REQUEST_LOGGING", {})

REQUEST_LOGGING_SETTINGS.update(user_settings)
