from django.db import models


class Vet(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    PLZ = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
