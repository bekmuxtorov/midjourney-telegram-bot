from django.contrib import admin
from .models import TelegramUser, Example, Permission, Request, Message


class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'get_username',
                    'tg_id', 'request_all_count']
    search_fields = ['full_name']


class ExampleAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'create_date']


class PermissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'permission_status']
    list_editable = ('permission_status',)
    list_display_links = None


class RequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'get_date']
    search_fields = ['user']


class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'get_username',
                    'get_date', 'get_message']
    search_fields = ['user']


admin.site.register(TelegramUser, TelegramUserAdmin)
admin.site.register(Example, ExampleAdmin)
admin.site.register(Permission, PermissionAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(Message, MessageAdmin)
