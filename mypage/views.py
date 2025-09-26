from django.shortcuts import render, redirect
from home.models import User, OrderItem
from mypage.models import WishList
from community.models import Comment, Post

# Create your views here.
def Profile(request, id):
    user = User.objects.get(id = id)
    comments = Comment.objects.filter(id=user.id).order_by("-created_at")
    posts = Post.objects.filter(id=user.id).order_by("-updated_at")
    context = {
        "user" : user,
        "comments" : comments,
        "reviews" : posts
    }

    return render(request, "users/profile.html", context)

def OrderList(request, id):
    items = OrderItem.objects.filter(id=id).order_by("-order__created_at")
    context = {
        "items" : items
    }
    return render(request, "mypage/order_list.html", context)

def MyWish(request, id):
    if id == id:
        wishes = WishList.objects.all()
        context = {
            "wishes" : wishes,
        }
    return render(request, "mypage/wish_list.html", context)

def WishDelete(request, id):
    shoe = WishList.objects.get(id=id)
    shoe.delete()
    conn_user = request.user.id
    return redirect(f"/mypage/{conn_user}/mywish/")