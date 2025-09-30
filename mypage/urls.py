from django.urls import path
from mypage import views

urlpatterns = [
    path("<int:id>/", views.Profile, name="profile"),
    # 장바구니
    path("cart/", views.CartList, name="cartlist"),
    # 주문목록
    path("<int:id>/order/", views.OrderList, name="orderlist"),
    # 위시리스트
    path("<int:id>/mywish/", views.MyWish, name="mywish"),
    # 내글관리
    path("mycommunty/", views.MyCommunty, name="mycommunty"),
    # 위시리스트삭제
    path("<int:id>/delete/", views.WishDelete, name="wish_delete"),
    # 장바구니 
]