from django.apps import AppConfig

def ready(self):
    import contact.signals

class ContactConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contact'