from django.urls import path
from mall import views

urlpatterns = [
    # 몰 메인
    path("", views.mall_main, name="mall_main"),
    # 상품(모두보기,런닝화종류1,런닝화종류2)
    path("product/", views.mall_product, name="product"),
    # 상품상세
    #path("product_detail/<str:category>/<int:id>/", views.mall_product_detail, name="product_detail"),
    path("product_detail/<int:id>/", views.mall_product_detail, name="product_detail"),
    # 장바구니
    path("cart/", views.mall_cart, name="cart"),
    # 장바구니 추가
    path("cart/add/", views.mall_cart_add, name="cart_add"),
    # 장바구니 삭제
    path("cart/remove/<int:id>/", views.mall_cart_remove, name="cart_remove"),
    # 상품결제
    path("parchase/", views.mall_parchase, name="parchase"),
    # 상품구매완료
    path("parchase_completed/", views.mall_parchase_completed, name="parchase_completed"),
    # 슈마커 크롤링 요청
    path("c/", views.crawling_shoes_page),
    # 쇼핑몰 후기 쓰기/수정
    path("mall_review/<int:shoe_id>/", views.mall_review, name="mall_review"),
    # 쇼핑몰 후기 상세 페이지
    path("mall_review_detail/<int:review_id>/", views.mall_review_detail, name="mall_review_detail"),
    # 쇼핑몰 후기 삭제 
    path("mall_review_delete/<int:id>/", views.mall_review_delete, name="mall_review_delete"),
]