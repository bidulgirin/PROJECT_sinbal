# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User, UserBio

# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = [
        (None, {"fields" : ("username", "password")}),
        ("개인정보", {"fields": ("first_name", "last_name", "email", "address", "gender")}),
        ("추가필드", {"fields": ("profile_image", "short_description", "nickname", "favorite_brand")}),
        ("권한", {"fields": ("is_active", "is_staff", "is_superuser", "is_admin")}),
        ("중요한 일정", {"fields": ("last_login", "date_joined")}),
    ]
    ordering = ('email',)
    
@admin.register(UserBio)
class UserBioAdmin(admin.ModelAdmin):
    list_display = ('user', 'shoe_size', 'ball_foot', 'favorite_brand')