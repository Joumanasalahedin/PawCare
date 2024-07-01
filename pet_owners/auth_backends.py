from django.contrib.auth.backends import BaseBackend
from .models import PetOwner


class PetOwnersBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = PetOwner.objects.get(username=username)
            if user.check_password(password):
                return user
        except PetOwner.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return PetOwner.objects.get(pk=user_id)
        except PetOwner.DoesNotExist:
            return None
