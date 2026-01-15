from django.apps import AppConfig

class DomainConfig(AppConfig):
    name = 'domain'

    verbose_name = 'Domain Layer'

    def ready(self):
         from . import models