from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models
from pet_owners.models import Pet


class VetManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        email = self.normalize_email(username)
        user = self.model(username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class Vet(AbstractBaseUser, PermissionsMixin):
    username = models.EmailField(unique=True, null=False)
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

    groups = models.ManyToManyField(Group, related_name='vet_users')
    user_permissions = models.ManyToManyField(
        Permission, related_name='vet_user_permissions')

    objects = VetManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name


class Appointments(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE,
                            null=True, related_name='pet_appointments')
    vet = models.ForeignKey(Vet, on_delete=models.CASCADE,
                            related_name='vet_appointments')
    date = models.DateField()
    time = models.TimeField()
    complaints = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment with {self.vet.name} for {self.pet.name} on {self.date} at {self.time}"
