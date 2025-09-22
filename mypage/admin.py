from django.contrib import admin
from home.models import Brand, Category, Shoe, Review, Marathon, Registration, Cart, Order, OrderItem

# Register your models here.
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Shoe)
admin.site.register(Review)
admin.site.register(Marathon)
admin.site.register(Registration)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)