from django.contrib import admin
#from mall.models import Example # 나중에 카테고리 모델 확정되면 변경 
from home.models import Brand, Category, Shoe
# Register your models here.

# 카테고리 slug 이용
class MallCategoryAdmin(admin.ModelAdmin):
    pass
    #list_display = ()
    # prepopulated_fields = {"slug": ("title",)}
  
admin.site.register(Category, MallCategoryAdmin)

class MallBrandAdmin(admin.ModelAdmin):
    pass
admin.site.register(Brand, MallBrandAdmin)
# 신발 모델 admin 에서 관리하는데 mall 쪽에서 관리해야하지 않을까 싶어서 일단 admin 추가
admin.site.register(Shoe)