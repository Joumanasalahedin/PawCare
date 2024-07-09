from django.db import models
from pet_owners.models import PetOwner
from vets.models import Vet


class Appointments(models.Model):
    owner = models.ForeignKey(PetOwner, on_delete=models.CASCADE)
    vet = models.ForeignKey(Vet, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    complaints = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment with {self.vet.name} for {self.pet_owner.name} on {self.date} at {self.time}"
