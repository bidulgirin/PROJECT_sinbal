import random
from django.shortcuts import render, redirect
from home.models import Shoe, Category, Marathon
from community.models import Post
from mypage.models import WishList
from datetime import *
from django.utils import timezone

# Create your views here.
def home(request):
    today = timezone.now().date()
    categorys = Category.objects.all()[:5]
    hot_shoes = Shoe.objects.all().order_by("-rating")[:6]
    # 자유 게시판 (category=1)
    free_post = Post.objects.filter(category = "free").order_by('-views')[:1]
    # 요청 게시판 (category=2)
    request_post = Post.objects.filter(category = "request").order_by('-views')[:1]
    # 신발리뷰 게시판 (category=3)
    review_post = Post.objects.filter(category = "review").order_by('-views')[:1]
    # 마라톤후기 게시판 (category=4)
    marathon_post = Post.objects.filter(category = "marathon").order_by('-views')[:1]
    # 마라톤
    marathons = Marathon.objects.all().order_by('-pk')[:3]
    
    # 추천기능
    # 위시리스트 혹은 좋아하는 브랜드가 입력되었을경우에 발동 (현재좋아하는브랜드컬럼이보이지않으므로걍 위시리스트에서가지고옴)
    recommend_list = []
    wishlist_data = WishList.objects.filter(user_id = request.user.id) 
    # wishlist_data 에서 나오는 shoe_id 를 모두 불러와서 random 돌림
    if len(wishlist_data) > 0:
        for i in wishlist_data:
            recommend_list.append(i.shoe_id)
        # 랜덤으로 하나 뽑는다
        random_item = random.choice(recommend_list)
        recommend_shoe = Shoe.objects.get(id=random_item)
        
    else :
        recommend_shoe = 0
        
    print(recommend_list)
            
    context = {
        "categorys": categorys,
        "hot_shoes": hot_shoes,
        "free_post" : free_post,
        "request_post" : request_post,
        "review_post" : review_post,
        "marathon_post" : marathon_post,
        "marathons" : marathons,
        "recommend_shoe" : recommend_shoe,
        }
    
        
        
    return render(request, "home/home.html", context)

