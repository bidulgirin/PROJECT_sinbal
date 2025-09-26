from django.contrib import admin
from home.models import Brand, Category, Shoe, Review, Marathon, Cart, Order, OrderItem
from mypage.models import WishList

# Register your models here.
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Shoe)
admin.site.register(Review)
admin.site.register(Marathon)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(WishList)