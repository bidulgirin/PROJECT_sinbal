from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True    

    def create_user(self, username, nickname, email, address, gender, password=None):
        if not email:
            raise ValueError("must haveu user email")
        
        if not password:
            raise ValueError("must have password")
        
        if not username:
            raise ValueError("must have username")
        
        user = self.model(
            nickname = nickname,
            email = self.normalize_email(email),
            username = username,
            gender = gender,
            address = address,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nickname, email, username, password=None): # is_staff, ... 등등을 보내주기위한 매개변수
        user = self.create_user(
            nickname=nickname,
            email=email,
            username=username,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self.db)
        
        return user

class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    USERNAME_FIELD = "email" # 로그인 ID로 사용할 필드임~
    REQUIRED_FIELDS = ["nickname", "username"]  # createsuperuser 할때 필요한거
    
    username = models.CharField("사용자 이름", max_length=5, unique=False)
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
