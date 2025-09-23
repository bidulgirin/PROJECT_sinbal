from django.db import models

# Create your models here.

# 상품 데이터 모델을 가져와야합니다
# 필수 컬럼은 slug 인데 이름을 category 로 변경해야할듯 싶다~
class Example(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=40)
    
    def __str__(self):
        return f"{self.title}"

class ExampleBrand(models.Model): 
    name = models.CharField(max_length=100) 
    
    def __str__(self): return self.name
    
class ExampleCategory(models.Model): 
    name = models.CharField(max_length=50) 
    
    def __str__(self): return self.name
        
# 예시 ( forienkey 로 카테고리 id 와 연결한 상품을 생각하고 만들것임) 
class ExampleProduct(models.Model):
        brand = models.ForeignKey(ExampleBrand, on_delete=models.CASCADE) 
        name = models.CharField(max_length=200) 
        price = models.IntegerField(default=0) 
        image_url = models.TextField(blank=True) 
        description = models.TextField(blank=True) 
        source_url = models.TextField() 
        categories = models.ManyToManyField(ExampleCategory) 
        weight = models.IntegerField(null=True, blank=True) 
        stock = models.IntegerField(default=0) 
        rating = models.FloatField(default=0) 
        created_at = models.DateTimeField(auto_now_add=True) 