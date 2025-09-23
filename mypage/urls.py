from django.urls import path
from mypage import views


urlpatterns = [
    path("<int:id>/", views.Profile, name="profile"),
    path("order/", views.OrderList, name="orderlist"),
    path("mywish/", views.MyWish, name="mywish"),
    path("<int:id>/delete/", views.WishDelete, name="wish_delete"),
]