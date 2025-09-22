from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models


class Brand(models.Model): 
    name = models.CharField(max_length=100)
    
    def __str__(self): return self.name
    
    
class Category(models.Model): 
    name = models.CharField(max_length=50) 
    
    def __str__(self): return self.name
    

class Shoe(models.Model): 
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE) 
    name = models.CharField(max_length=200) 
    price = models.IntegerField() 
    image_url = models.TextField(blank=True) 
    description = models.TextField(blank=True) 
    source_url = models.TextField() 
    categories = models.ManyToManyField(Category) 
    weight = models.IntegerField(null=True, blank=True) 
    stock = models.IntegerField(default=0) 
    rating = models.FloatField(default=0) 
    created_at = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self): return f"{self.brand.name} {self.name}"
    
class Review(models.Model): 
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE) 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    rating = models.IntegerField() 
    title = models.CharField(max_length=200) 
    content = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self): 
        return f"{self.shoe.name} - {self.rating}점"
    
class Marathon(models.Model): 
    name = models.CharField(max_length=200) 
    date = models.DateField() 
    location = models.CharField(max_length=200) 
    distance = models.CharField(max_length=50) 
    price = models.IntegerField() 
    website_url = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self): return self.name

# 마라톤 대리 등록~
class Registration(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    marathon = models.ForeignKey(Marathon, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self): 
        return f"{self.user.username} - {self.marathon.name}"
    
    
class Cart(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE) 
    size = models.CharField(max_length=10) 
    quantity = models.IntegerField(default=1) 
    created_at = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self): return f"{self.user.username}의 장바구니"
    
class Order(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    total_price = models.IntegerField() 
    name = models.CharField(max_length=50) 
    phone = models.CharField(max_length=20) 
    address = models.TextField() 
    status = models.CharField(max_length=20, default='주문완료') 
    created_at = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self): return f"주문번호 {self.id}"
    
class OrderItem(models.Model): 
    order = models.ForeignKey(Order, on_delete=models.CASCADE) 
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE) 
    size = models.CharField(max_length=10) 
    quantity = models.IntegerField() 
    price = models.IntegerField() 
    
    def __str__(self): 
        return f"{self.shoe.name} x {self.quantity}"