from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class PetOwnerManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class PetOwner(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True, null=False)
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    street = models.CharField(max_length=200, null=True)
    PLZ = models.IntegerField(null=True)
    phone_number = models.CharField(max_length=15, null=True)
    email = models.EmailField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = PetOwnerManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name
