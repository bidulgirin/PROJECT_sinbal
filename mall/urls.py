from django.urls import path
from mall import views

urlpatterns = [
    # 몰 메인
    path("", views.mall_main, name="mall_main"),
    # 상품(모두보기,런닝화종류1,런닝화종류2)
    path("product/<slug:slug>/", views.mall_product, name="product"),
    # 상품상세
    #path("product_detail/<str:category>/<int:id>/", views.mall_product_detail, name="product_detail"),
    path("product_detail/<int:id>/", views.mall_product_detail, name="product_detail"),
    # 상품결제
    path("parchase/", views.mall_parchase, name="parchase"),
    # 삼품구매완료
    path("parchase_completed/", views.mall_parchase_completed, name="parchase_completed"),
]