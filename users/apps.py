from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    #Se importa aca adentro para hacer un safe import y que no ocurran problemas
    def ready(self):
        import users.signals
