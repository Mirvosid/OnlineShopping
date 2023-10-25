from django.db import models
import uuid
from product.models import Product
from shopcard.models import ShopCard

# Create your models here.
class Items(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, null=False, primary_key=True)
    product_id = models.ForeignKey(Product,null=True, blank=True, on_delete=models.CASCADE)
    shopcard_id = models.ForeignKey(ShopCard,null=True, blank=True, on_delete=models.CASCADE)
    sell_date = models.DateTimeField()

    def __str__(self) -> str:
        return str(self.product_id)