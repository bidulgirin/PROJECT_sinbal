from django.shortcuts import render, redirect
from home.models import User, OrderItem
from mypage.models import WishList
from django.views.decorators.http import require_POST
from django.urls import reverse
from community.models import Comment, Post

# Create your views here.
def Profile(request, id):
    user = User.objects.get(id = id)
    comments = Comment.objects.filter(id=user.id)
    posts = Post.objects.filter(id=user.id)
    context = {
        "user" : user,
        "comments" : comments,
        "reviews" : posts
    }

    return render(request, "users/profile.html", context)

def OrderList(request, id):
    items = OrderItem.objects.filter(id=id)
    context = {
        "items" : items
    }
    return render(request, "mypage/order_list.html", context)

def MyWish(request):
    return redirect("mypage/mywish/")

def WishDelete(reqeust, id):
    shoe = OrderItem.objects.get(id=id)
    shoe.delete()
    return redirect("/mypage/mywish/")