import time
import json

from .models import RequestLog
from .settings import REQUEST_LOGGING_SETTINGS
import logging

logger = logging.getLogger('request_log')


def get_ip_client(request):
    client_ip_address = request.META.get('HTTP_IP_ADDRESS')
    if client_ip_address:
        return client_ip_address

    x_cf_connecting_ip = request.META.get('HTTP_CF_CONNECTING_IP')
    if x_cf_connecting_ip:
        ip = x_cf_connecting_ip.split(',')[0]
    else:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
    return ip


class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        start_at = time.time()

        response = self.get_response(request)
        if not REQUEST_LOGGING_SETTINGS['ENABLE_PYTHON_LOG'] and not REQUEST_LOGGING_SETTINGS['ENABLE_DB_LOG']:
            return response

        try:
            if request.path in REQUEST_LOGGING_SETTINGS['WHITELIST_PATHS']:
                return response

            client_ip = get_ip_client(request)
            data = {
                'user_id': request.user.id if request.user else None,
                'method': request.method,
                'hostname': request.META.get('HTTP_HOST', ''),
                'path': request.path,
                'request_params': request.GET,
                'client_ip': client_ip,
                'user_agent': request.META.get('HTTP_USER_AGENT', ''),
                'response_code': response.status_code,
                'response_time': time.time() - start_at,
            }

            if REQUEST_LOGGING_SETTINGS['ENABLE_DB_LOG']:
                RequestLog.objects.create(**data)

            if REQUEST_LOGGING_SETTINGS['ENABLE_PYTHON_LOG']:
                logger.info('%s %s %s %s %s %s "%s"',
                            data['method'], data['path'], data['response_code'], int(data['response_time'] * 1000),
                            data.get('user_id', '-'), data['client_ip'], data['user_agent'])
            
        except Exception as e:
            logger.exception(e)

        return response
