from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

class UserManager(BaseUserManager):
    use_in_migrations = True    

    def create_user(self, nickname, email, username, password=None):
        
        user = self.model(
            nickname = nickname,
            email = self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nickname, password=None, **kwargs): # is_staff, ... 등등을 보내주기위한 매개변수
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_admin", True)

        return self.create_user(nickname, password, **kwargs)

class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    USERNAME_FIELD = "nickname" # 로그인 ID로 사용할 필드임~
    REQUIRED_FIELDS = ["email", "username"]  # createsuperuser 할때 필요한거
    
    username = models.CharField("사용자 이름", max_length=50, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    nickname = models.CharField("닉네임", max_length=10, blank=False, unique=True)
    email = models.EmailField("이메일", max_length=254, blank=False, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    profile_image = models.ImageField("프로필 이미지", blank=True, null=True)
    short_description = models.TextField("소개글", blank=True, default='')
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.CharField("상세주소", max_length=100, default='', blank=True)

    GENDER = (
        ("Female", "여성"),
        ("Male", "남성"),
    )
    gender = models.CharField("성별", max_length=10, choices=GENDER, default="Female")

    
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