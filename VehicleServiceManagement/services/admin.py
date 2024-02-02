from django.contrib import admin
from .models import Vehicle, Service  # Import your models

admin.site.register(Vehicle)  # Register the Vehicle model
admin.site.register(Service)  # Register the Service model
