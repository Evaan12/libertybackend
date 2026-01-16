# domain/apps.py

from django.apps import AppConfig

class DomainConfig(AppConfig):
    name = 'domain'
    verbose_name = 'Domain Layer'

    def ready(self):
        # Import signals to ensure they are connected
        from . import signals