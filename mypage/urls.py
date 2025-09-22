from django.urls import path
from mypage import views


urlpatterns = [
    path("<int:id>/", views.UserInfo),
    path("order/", views.OrderList),
    path("mywish/", views.MyWish),
    path("<int:id>/delete/", views.WishDelete, name="wish_delete"),
]