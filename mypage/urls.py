from django.urls import path
from mypage import views

urlpatterns = [
    path("<int:id>/", views.Profile, name="profile"),
    # 주문목록
    path("<int:id>/order/", views.OrderList, name="orderlist"),
    # 위시리스트
    path("<int:id>/mywish/", views.MyWish, name="mywish"),
    # 위시리스트삭제
    path("<int:id>/delete/", views.WishDelete, name="wish_delete"),
]