from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models
from django.apps import apps


class PetOwnerManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class PetOwner(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True, null=False)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=200, null=True)
    street = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    email = models.EmailField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, related_name='pet_owners_users')
    user_permissions = models.ManyToManyField(
        Permission, related_name='pet_owners_user_permissions')

    objects = PetOwnerManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name


class Pet(models.Model):
    owner = models.ForeignKey(
        PetOwner, on_delete=models.CASCADE, related_name='pets')
    vet = models.ForeignKey('vets.Vet', on_delete=models.CASCADE,
                            null=True, related_name='pets')
    name = models.CharField(max_length=100, null=False)
    breed = models.CharField(max_length=100, null=False, blank=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[
                              ('male', 'Male'), ('female', 'Female')])
    weight = models.FloatField(null=True, blank=True)
    vaccinations = models.TextField(null=True, blank=True)
    medical_notes = models.TextField(null=True, blank=True)
    previous_reports = models.TextField(null=True, blank=True)
    additional_comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
