from django.db import models
#
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # models.ImageField 이미지 파일 올릴거임 / upload_to = users 폴더 안에 profile 폴더안에 업로드하겠다
    profile_image = models.ImageField("프로필 이미지", upload_to="users/profile", blank=True)
    short_description = models.TextField("소개글", blank=True)
    like_posts = models.ManyToManyField(
        "posts.Post",
        verbose_name = "좋아요 누른 Post 목록", # 관리자 페이지에서 사용할 속성 설명
        related_name = "like_users", # 역방향으로 접근할 때 related_name 값으로 코드 작성해야 함. / 여기선 좋아요 누른 user 쪽으로 가고 싶을 때 사용
        blank = True,
    )
    following = models.ManyToManyField(
        "self",
        verbose_name = "팔로우 중인 사용자들",
        related_name = "followers",
        symmetrical = False,
        through = "users.Relationship",
    )

    def __str__(self):
        return self.username
    
class Relationship(models.Model):
    from_user = models.ForeignKey(
        "users.User",
        verbose_name = "팔로우를 요청한 사용자",
        related_name = "following_relationships", # 나를 팔로우 하는 사람들을 찾고 싶을 때
        on_delete = models.CASCADE,
    )
    to_user = models.ForeignKey(
        "users.User",
        verbose_name = "팔로우 요청의 대상",
        related_name = "follower_relationships", # 내가 팔로우 하는 사람을 찾을 때
        on_delete = models.CASCADE,
    )
    created = models.DateTimeField(auto_now_add = True) # 관계가 설정된 시간

    def __str__(self):
        return f"관계 ({self.from_user} -> {self.to_user})"