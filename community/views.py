from django.shortcuts import redirect, render
from community.models import Post, Comment, PostImage
from datetime import *
from django.utils import timezone
from community.forms import PostForm

# Create your views here.
def community(request):
    today = timezone.now().date()
    # 오늘을 기준으로 해서 인기,조회 순으로 3개만 보여줄것임
    # 전체 Post 글 중에 좋아요 인기글(일주일)
    weeks_best_posts = Post.objects.filter(created_at__gte = timezone.now() - timedelta(days=7)).order_by('-views')[:3]
    # 전체 Post 글 중에 실시간 인기글
    best_posts = Post.objects.filter(created_at__gte = today).order_by('-views')[:3]
    # 전체 게시판
    posts = Post.objects.all().order_by("-pk")
    # 자유 게시판 (category=1)
    free_posts = Post.objects.filter(category = "free")
    # 요청 게시판 (category=2)
    request_posts = Post.objects.filter(category = "request")
    # 신발리뷰 게시판 (category=3)
    review_posts = Post.objects.filter(category = "review")
    # 마라톤후기 게시판 (category=4)
    marathon_posts = Post.objects.filter(category = "marathon")
    
    context = {
        "weeks_best_posts": weeks_best_posts,
        "best_posts": best_posts,
        "posts":posts,
        "free_posts":free_posts,
        "request_posts":request_posts,
        "review_posts":review_posts,
        "marathon_posts":marathon_posts,
        "today": today
    }
    
    return render(request, "community/community.html", context)

# 포스트 게시하기
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            # 다중 이미지 넣기
            for image_file in request.FILES.getlist("images"):
                PostImage.objects.create(
                    post=post, 
                    images=image_file
            )
            # 해당 포스트의 상세페이지로 감
            return redirect("community:product_detail", id=post.id)
    form = PostForm()
    
    context = {
        "form": form
    }
    return render(request, "community/community_post.html", context)

# 글 수정
def edit_post(request, id):
    
    data = Post.objects.get(id = id)
    
    if request.method == "POST":
        form = PostForm(request.POST, instance = data)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            # 다중 이미지 넣기
            for image_file in request.FILES.getlist("images"):
                PostImage.objects.create(
                    post=post, 
                    images=image_file
            )
            # 해당 포스트의 상세페이지로 감
            return redirect("community:product_detail", id=post.id)
    else:
        form = PostForm(instance = data)
    context = {
        "form" : form, 
    }
    return render(request, "community/community_post.html", context)

# 글 삭제
def delete_post(request, id):
    # Cart 에서 등록된 상품 id 를 가져온다
    delete_data = Post.objects.get(id = id)
    delete_data.delete()
    return redirect('community:community') # 일단 메인으로 돌려보내

# 상세페이지
def product_detail(request, id):
    data = Post.objects.get(id = id)
    context = {
        "data": data
    }
    return render(request, "community/community_post_detail.html", context)