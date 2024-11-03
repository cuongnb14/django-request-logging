from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class RequestLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='request_logs',
                             null=True, blank=True, default=None)
    method = models.CharField(max_length=15)
    hostname = models.CharField(max_length=255)
    path = models.CharField(max_length=1500)
    request_params = models.JSONField(null=True, blank=True, default=None)
    client_ip = models.CharField(max_length=255)
    headers = models.JSONField(default=dict)
    response_code = models.IntegerField()
    response_time = models.FloatField()
    request_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.path
