from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

class User(AbstractUser):
    profile_image = models.ImageField(
        "프로필 이미지", upload_to = "users/profile", blank = True
    )
    short_description = models.TextField("소개글", blank=True)
    nickname = models.CharField(max_length = 10, null=False, blank=False)
    favorite_brands = models.CharField(max_length = 20, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    size = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.nickname}"