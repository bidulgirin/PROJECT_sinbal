from django.shortcuts import render, redirect
from home.models import Shoe, Category
from community.models import Post
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

    context = {
        "categorys": categorys,
        "hot_shoes": hot_shoes,
        "free_post" : free_post,
        "request_post" : request_post,
        "review_post" : review_post,
        "marathon_post" : marathon_post,
    }
    return render(request, "home/home.html", context)