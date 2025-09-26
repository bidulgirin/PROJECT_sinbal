# mypage/models.py

from django.db import models
from home.models import Shoe
from users.models import User
from django.utils import timezone
# Create your models here.

class WishList(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(default=timezone.now)