from django.shortcuts import render, redirect
from home.models import OrderItem
from django.views.decorators.http import require_POST
from django.urls import reverse
from community.models import Comment, Post
from users.models import User

# Create your views here.

# 개인 프로필 뷰
def Profile(request, id):
    user = User.objects.get(id = id)
    comments = Comment.objects.filter(id=user.id)
    posts = Post.objects.filter(id=user.id)
    # User의 이름, 프로필, 댓글, 리뷰 가 필요하기에 데이터 넘겨줌
    context = {
        "user" : user,
        "comments" : comments,
        "reviews" : posts,
    }

    return render(request, "users/Profile.html", context)

# 주문 목록 뷰
def OrderList(request, id):
    # 주문된 아이템들의 목록을 가져옴
    items = OrderItem.objects.filter(id=id)
    context = {
        "items" : items
    }
    return render(request, "mypage/order_list.html", context)

# 위시리스트 뷰 / nav에 연결할 예정
def MyWish(request):
    return redirect("mypage/mywish/")

# 위시리스트 지우기
def WishDelete(reqeust, id):
    shoe = OrderItem.objects.get(id=id)
    shoe.delete()
    # 지우는게 완료되면 다시 위시리스트 페이지로 리다이렉트
    return redirect("/mypage/mywish/")