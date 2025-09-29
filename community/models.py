# community/models.py
from django.db import models
from users.models import User

class Post(models.Model):
    CATEGORY = (
        ('all', '전체 게시판'),
        ('free', '자유 게시판'),
        ('request', '요청 게시판'),
        ('review', '신발 리뷰'),
        ('marathon', '마라톤 후기'),
    )
    
    users = models.ForeignKey("users.User",
                              verbose_name = "작성자",
                              on_delete = models.CASCADE)
    title = models.CharField(max_length=50, verbose_name = "제목")
    content = models.TextField(verbose_name = "내용")
    post_category = models.CharField(max_length = 20, choices = CATEGORY, default = "free", verbose_name="게시판") #* 자유 게시판을 기본으로 해둠
    image = models.ImageField(upload_to = "posts/", blank = True, null = True, verbose_name = "이미지")
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = "작성일")
    updated_at = models.DateTimeField(auto_now = True, verbose_name = "수정일")
    likes = models.ManyToManyField("users.User", related_name = "like_users", blank = True)
    views = models.PositiveIntegerField(default = 0, verbose_name = "조회수")
        
    def __str__(self):
        return self.title
    
class PostImage(models.Model):
    post = models.ForeignKey(Post, verbose_name = "포스트", on_delete = models.CASCADE)
    photo = models.ImageField("사진", upload_to="post")
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = "comments")
    user = models.ForeignKey("users.User", on_delete = models.CASCADE, verbose_name = "작성자")
    content = models.TextField(verbose_name = "댓글 내용")
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = "작성일")
        
    def __str__(self):
        return f"{self.post.title}의 댓글"
    
