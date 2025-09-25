# home/models.py
from django.db import models
from users.models import User


class Brand(models.Model): 
    name = models.CharField(max_length=100)
    brand_img = models.ImageField(upload_to="brand/", blank = True)
    
    def __str__(self): return self.name
    
    
class Category(models.Model): 
    name = models.CharField(max_length=50) 
    
    def __str__(self): return self.name
    

class Shoe(models.Model):
    CATEGORY = (
        ('VG', '매우좋음'),
        ('G', '좋음'),
        ('N', '보통'),
    )
        
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE) 
    name = models.CharField(max_length=200) 
    price = models.IntegerField(default=0) 
    images = models.ImageField(upload_to="reviews/", blank = True, null = True) 
    description = models.TextField(blank=True) 
    source_url = models.TextField() 
    categories = models.ManyToManyField(Category) 
    weight = models.IntegerField(default=0, null=True, blank=True) 
    stock = models.IntegerField(default=0)
    comfort = models.CharField(max_length = 5, choices=CATEGORY, blank = True, default="")
    rating = models.FloatField(default=0) 
    created_at = models.DateTimeField(auto_now_add=True) 
        
    def __str__(self): return f"{self.brand.name} {self.name}"
    
class Review(models.Model): 
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE) 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    rating = models.IntegerField(default=0) 
    title = models.CharField(max_length=200) 
    content = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True) 
    color = models.CharField(max_length=10, blank = True, default = "")
    size = models.IntegerField(default=0)
    ball_foot = models.FloatField(default=0) # 발볼
    instep_foot = models.FloatField(default=0) # 발등
    Comfort = models.CharField(max_length = 5, blank=True, default="") # 착화감
    
    def __str__(self): 
        return f"{self.shoe.name} - {self.rating}점"
    
class Marathon(models.Model): 
    name = models.CharField(max_length=200) 
    date = models.DateField() 
    location = models.CharField(max_length=200) 
    distance = models.CharField(max_length=50) 
    price = models.IntegerField(default=0) 
    website_url = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self): return self.name
    
class Cart(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE) 
    size = models.CharField(max_length=10) 
    quantity = models.IntegerField(default=1) 
    created_at = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self): return f"{self.user.username}의 장바구니"
    
class Order(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    total_price = models.IntegerField(default=0) 
    name = models.CharField(max_length=50) 
    phone = models.CharField(max_length=20) 
    addr_num = models.TextField(null=True, blank = True) # 우편번호 필드 
    address = models.TextField(null = True, blank = True)
    detail_address = models.TextField() # 상세 주소 필드 
    order_message = models.TextField(default='', blank=True) # 요청사항
    pay_method = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default='주문완료') 
    created_at = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self): return f"주문번호 {self.id}"
    
class OrderItem(models.Model): 
    order = models.ForeignKey(Order, on_delete=models.CASCADE) 
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE) 
    size = models.CharField(max_length=10) 
    quantity = models.IntegerField(default=0) 
    price = models.IntegerField(default=0) 
    
    def __str__(self): 
        return f"{self.shoe.name} x {self.quantity}"
    
   