import logging

from datetime import timedelta
from django.core.management import BaseCommand
from django.utils import timezone
from ...models import RequestLog

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument('keep', type=str, help='time range to keep request log: 1d (day), 1m (month)')


    def handle(self, *args, **options):
        keep = options.get('keep')
        value = int(keep[:-1])
        unit = keep[-1:]

        now = timezone.now()
        if unit == 'd':
            min_request_at = now - timedelta(days=value)
        elif unit == 'm':
            min_request_at = now - timedelta(days=value * 30)
        
        logger.info('delete request log before %s', min_request_at)
        RequestLog.objects.filter(request_at__lt=min_request_at).delete()
        logger.info('delete request log before %s done', min_request_at)