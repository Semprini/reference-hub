from django.apps import AppConfig
from django.db.models.signals import post_save, post_delete
from django.conf import settings


class SyncConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sync'

    def ready(self):
        try:
            from .signals import init_signals
            init_signals()
            print("Custom Signals Initialised")
        except ImportError:
            print("No Custom Signals")
