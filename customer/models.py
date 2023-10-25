from django.db import models
import uuid

# Create your models here.
class Customer(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, null=False, primary_key=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=30, null=True, blank=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.name