from django.db import models
import uuid

# Create your models here.
class Customer(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False, null=False)
    name = models.CharField(max_length=300, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=30, null=True, blank=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.name