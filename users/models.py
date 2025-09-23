# users/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

# models.py에서 마이그레이션할 때 기본값 설정
class User(AbstractUser):
    profile_image = models.ImageField("프로필 이미지", blank=True, null=True)
    short_description = models.TextField("소개글", blank=True, default='')
    nickname = models.CharField(max_length=10, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    size = models.IntegerField(blank=True, null = True, default = 0)
    
class UserBio(models.Model):
    CATEGORY = (
        ('XN', '매우좁음'),
        ('N', '좁음'),
        ('R', '보통'),
        ('W', '넓음'),
        ('XW', '매우넓음'),
    )
    shoe_size = models.IntegerField("신발 사이즈", default="0")
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = "foot_info")
    ball_foot = models.CharField("발볼 크기", max_length = 5, choices = CATEGORY, default="R")
    favorite_brand = models.CharField(max_length=10, blank=True, null=True)
    
