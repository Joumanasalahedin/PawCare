from django.db import models


class Recreation(models.Model):
    CATEGORY_CHOICES = [
        ('trail', 'Dog Trail'),
        ('park', 'Dog Park'),
        ('grooming', 'Grooming Service'),
        ('boarding', 'Boarding House'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.name
