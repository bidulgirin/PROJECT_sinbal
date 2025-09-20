from django.db import models

# Create your models here.

# 상품 데이터 모델을 가져와야합니다
# 필수 컬럼은 slug 인데 이름을 category 로 변경해야할듯 싶다~
class Example(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=40)
    
    def __str__(self):
        return f"{self.title}"
    
# 예시 ( forienkey 로 카테고리 id 와 연결한 상품을 생각하고 만들것임) 
class ExampeProduct(models.Model):
    pass