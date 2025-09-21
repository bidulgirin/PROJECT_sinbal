from django.urls import path
from mall import views

urlpatterns = [
    # 몰 메인
    path("", views.mall_main, name="mall_main")
]