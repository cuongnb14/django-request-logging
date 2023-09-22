from django.contrib import admin

from .models import RequestLog


@admin.register(RequestLog)
class RequestLogAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'client_ip', 'hostname', 'method', 'path', 'response_code', 'display_response_time',
                    'request_at')
    search_fields = ('client_ip', 'path', 'user__username')

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'user', 'client_ip', 'user_agent',
                )
            }
        ),
        (
            'Request',
            {
                'fields': (
                    'hostname', ('method', 'path'), 'display_request_params',
                    'request_at',
                )
            }
        ),
        (
            'Response',
            {
                'fields': (
                    'response_code', 'display_response_time'
                )
            }
        ),
    )

    @admin.display(description='response time', ordering='response_time')
    def display_response_time(self, obj):
        if obj.response_time:
            return "{:.2f}".format(obj.response_time)
        return self.get_empty_value_display()

    @admin.display(description='request params')
    def display_request_params(self, obj):
        return self.format_json(obj.request_params) if obj.request_params else '-'

    def has_change_permission(self, request, obj=None):
        return False
