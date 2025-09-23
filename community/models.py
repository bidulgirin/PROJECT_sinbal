# community/models.py

from django.db import models
from users.models import User
from sinbal_pj import settings


class Post(models.Model):
    CATEGORY = (
        ('all', '전체 게시판'),
        ('free', '자유 게시판'),
        ('request', '요청 게시판'),
        ('review', '신발 리뷰'),
        ('marathon', '마라톤 후기'),
    )
    
    title = models.CharField(max_length=50, verbose_name = "제목")
    content = models.TextField(verbose_name = "내용")
    category = models.CharField(max_length = 20, choices = CATEGORY, default = "free", verbose_name="게시판") #* 자유 게시판을 기본으로 해둠
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = "작성자")
    image = models.ImageField(upload_to = "posts/", blank = True, null = True, verbose_name = "이미지")
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = "작성일")
    updated_at = models.DateTimeField(auto_now = True, verbose_name = "수정일")
    likes = models.ManyToManyField(User, related_name = "like_posts", blank = True)
    views = models.PositiveIntegerField(default = 0, verbose_name = "조회수")
    
    
    class Meta:
        verbose_name = "게시글"
        verbose_name_plural = "게시글"
        
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = "comments")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, verbose_name = "작성자")
    content = models.TextField(verbose_name = "댓글 내용")
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = "작성일")
    
    class Meta:
        verbose_name = "댓글"
        verbose_name_plural = "댓글"
        
    def __str__(self):
        return f"{self.post.title}의 댓글"
    
