from django.apps import AppConfig


class RequestLoggingConfig(AppConfig):
    name = 'request_logging'
    verbose_name = 'Request Logging'

    def ready(self):
        pass
