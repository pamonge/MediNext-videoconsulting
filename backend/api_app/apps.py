from django.apps import AppConfig


class ApiAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_app'

    def ready(self):
        """
        Importar las signals cuando la app esté lista
        """
        import api_app.signals