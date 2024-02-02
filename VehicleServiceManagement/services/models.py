from django.db import models
from django.conf import settings

class Vehicle(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

class Service(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    service_date = models.DateField()
    description = models.TextField()
    expense = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    reminder_date = models.DateField(blank=True, null=True)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True)
    


