# mall/models.py
from django.db import models
from users.models import User
from home.models import Shoe

# 쇼핑몰후기 테이블 작성
class MallReview(models.Model):
    # 후기를 쓴사람의 Bio 데이터를 끌고 들어갈꺼에욥
    shoe = models.ForeignKey(Shoe, on_delete=models.SET_NULL, null=True )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=30)
    content = models.TextField(blank=True, null=True)
    image =  models.ImageField(upload_to="mall_reviews/%Y/%m/%d/", blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    rating = models.IntegerField(default=1)

# 다중이미지를 위한 
class MallReviewImage(models.Model):
    review = models.ForeignKey(MallReview, 
                             verbose_name= "리뷰 이미지", 
                             on_delete = models.CASCADE)
    images = models.ImageField("사진", upload_to="mall_reviews/%Y/%m/%d/", blank = True, null = True)