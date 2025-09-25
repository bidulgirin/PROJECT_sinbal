# users/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

# models.py에서 마이그레이션할 때 기본값 설정
class User(AbstractUser):
    GENDER = (
        ('Female', '여성'),
        ('Male', '남성')
    )
    
    profile_image = models.ImageField("프로필 이미지", blank=True, null=True)
    short_description = models.TextField("소개글", blank=True, default='')
    nickname = models.CharField("닉네임", max_length=10, blank=True, default='', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField("이메일", max_length=254, default = '', blank = True)
    address = models.CharField("상세주소", max_length=100, default='', blank=True)
    gender = models.CharField("성별", max_length=10, choices = GENDER, default = "F")

class UserBio(models.Model):
    CATEGORY = (
        ('Narrow', '좁음'),
        ('Regular', '보통'),
        ('Wide', '넓음'),
    )
    shoe_size = models.IntegerField("신발 사이즈", default="0")
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = "foot_info")
    ball_foot = models.CharField("발볼 크기", max_length = 10, choices = CATEGORY, default="R")
    favorite_brand = models.CharField("선호 브랜드", max_length=10, blank=True, null=True)
