from django.contrib import admin
from mall.models import Example # 나중에 카테고리 모델 확정되면 변경 

# Register your models here.
class MallAdmin(admin.ModelAdmin):
  #list_display = ()
  prepopulated_fields = {"slug": ("title",)}
  
admin.site.register(Example, MallAdmin)