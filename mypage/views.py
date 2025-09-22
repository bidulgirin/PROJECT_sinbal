from django.shortcuts import render, redirect
from home.models import User, Shoe, OrderItem
from mypage.models import WishList
from django.views.decorators.http import require_POST
from django.urls import reverse

# Create your views here.
def UserInfo(request, id):
    user = User.objects.filter(id = id)

    context = {
        "user" : user,
        "comments" : user.comment,
        "reviews" : user.review
    }

    return render(request, "user_info.html", context)

def OrderList(request, id):
    items = OrderItem.objects.filter(id=id)
    context = {
        "items" : items
    }
    return render(request, "mypage/order_list.html", context)

def MyWish(request, id):
    shoes = WishList.objects.filter(id=id)
    return redirect("mypage/mywish/")

def WishDelete(reqeust, id):
    shoe = OrderItem.objects.get(id=id)
    shoe.delete()
    return redirect("/mypage/mywish/")