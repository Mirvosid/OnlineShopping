from django.db import models
from category.models import Category
import uuid

# Create your models here.
class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, null=False, primary_key=True)
    name = models.CharField(max_length=300, null=True, blank=True)
    category_id = models.ForeignKey(Category,null=True, blank=True, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=20, decimal_places=5)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    

    def __str__(self):
        return self.name