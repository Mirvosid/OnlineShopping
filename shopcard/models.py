from django.db import models
from customer.models import Customer
import uuid

# Create your models here.
class ShopCard(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False, null=False)
    date = models.DateTimeField()
    owner = models.ForeignKey(Customer,null=True, blank=True, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=20, decimal_places=2)
    payment = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.owner)