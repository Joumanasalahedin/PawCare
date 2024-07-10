from django.db import models


class Recreation(models.Model):
    CATEGORY_CHOICES = [
        ('trail', 'Dog Trail'),
        ('park', 'Dog Park'),
        ('grooming', 'Grooming Service'),
        ('boarding', 'Boarding House'),
        ('care', 'Day Care'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    street = models.CharField(max_length=200, blank=True)
    PLZ = models.IntegerField(null=True)
    website = models.URLField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.name
