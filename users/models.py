from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # models.ImageField 이미지 파일 올릴거임 / upload_to = users 폴더 안에 profile 폴더안에 업로드하겠다
    profile_image = models.ImageField("프로필 이미지", upload_to="users/profile", blank=True)
    short_description = models.TextField("소개글", blank=True)
    
    def __str__(self):
        return self.username