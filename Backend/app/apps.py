from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):
        from .jobs import StartScheduler
        from .signals import add_user_to_default_group

        print('Django App is Ready!!!')

        StartScheduler()