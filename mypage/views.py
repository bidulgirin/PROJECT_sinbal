from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from home.models import OrderItem, Review, Cart
from mall.models import MallReview
from mypage.models import WishList
from community.models import Comment, Post
from users.models import User, UserBio
from django.contrib.auth.decorators import login_required
from users.models import User

# Create your views here.
@login_required(login_url = "login")
def Profile(request, id):
    
    user = get_object_or_404(User, id = id)
    if request.user.id != user.id:
        return redirect("/")
    
    # 관리자계정일경우에 에러나는거
    try: 
        userbio = UserBio.objects.get(user_id = id)
    except:
        userbio = [{}]
    
    comments = Comment.objects.filter(id=user.id).order_by("-created_at")
    reviews = Review.objects.filter(id=user.id).order_by("-created_at")
    
    context = {
        "user" : user,
        "comments" : comments,
        "reviews" : reviews,
        "userbio" : userbio,
    }

    return render(request, "users/profile.html", context)

def OrderList(request, id):
    items = OrderItem.objects.filter(id=id).order_by("-order__created_at")
    context = {
        "items" : items
    }
    return render(request, "mypage/order_list.html", context)
# 장바구니 리스트
def CartList(request):
    conn_user = request.user

    user_id = conn_user.id
    cart_datas = Cart.objects.filter(user_id=user_id)
    context = {
        "cart_datas" : cart_datas,
    }

    if request.method == "POST" :
        # 살 shoe_id 의 배열을 같이 보낸다.
        ids = request.POST.getlist("shoe_id[]")
        # 장바구니에 담았던 shoe_id 중 선택한 애들만 결제페이지로 보냄
        # get 으로 받으렴
        return redirect(reverse('parchase') + f'?id[]={ids}')

    return render(request, "mypage/cart_list.html", context)

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
# 내 글 보기
def MyCommunty(request):
    conn_user = request.user
    # 내 포스트
    posts = Post.objects.filter(author_id = conn_user.id)
    # 내 리뷰
    reviews = MallReview.objects.filter(user= conn_user.id)
    # 내 댓글
    comments = Comment.objects.filter(author_id = conn_user.id)

    context = {
        "posts" : posts,
        "reviews" : reviews,
        "comments" : comments,
    }
    return render(request, "mypage/my_post.html", context)