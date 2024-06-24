from django.contrib.auth.backends import BaseBackend
from .models import Vet


class VetBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Vet.objects.get(username=username)
            if user.check_password(password):
                return user
        except Vet.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Vet.objects.get(pk=user_id)
        except Vet.DoesNotExist:
            return None
