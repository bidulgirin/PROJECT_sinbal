from django.db import models
from home.models import Shoe
# Create your models here.
class WishList(models.Model):
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    size = models.IntegerField()
    quantity = models.IntegerField()