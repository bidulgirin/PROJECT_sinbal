from django.shortcuts import redirect, render
from community.models import Post, Comment, PostImage
from home.models import Marathon
from datetime import *
from django.utils import timezone
from community.forms import PostForm, CommentForm
from django.db.models import Q # 모델의 데이터를 불러올때 조건값을 붙이기 위함 
from django.views.decorators.http import require_POST

from django.core.paginator import Paginator # 페이지네이션
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
    # create 인지 update 인지 판단

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
            return redirect("community:post_detail", id=post.id)
    form = PostForm()
    
    context = {
        "form": form,
    }
    return render(request, "community/community_post.html", context)

# 글 수정
def edit_post(request, id):
    is_update = 0
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
            return redirect("community:post_detail", id=post.id)
    else:
        form = PostForm(instance = data)
        is_update = 1
    context = {
        "form" : form, 
        "is_update" : is_update,
    }
    return render(request, "community/community_post.html", context)

# 글 삭제
def delete_post(request, id):
    # Cart 에서 등록된 상품 id 를 가져온다
    delete_data = Post.objects.get(id = id)
    delete_data.delete()
    return redirect('community:community') # 일단 메인으로 돌려보내

# 상세페이지
def post_detail(request, id):
    data = Post.objects.get(id = id)
    commentForm = CommentForm()
    
    # 조회수 기능
    Post.objects.filter(id = id).update(views = data.views + 1 )
    
    context = {
        "data": data,
        "form" : commentForm,
    }
    
    return render(request, "community/community_post_detail.html", context)


# 마라톤 상세페이지
def marathon(request, id ):
    data = Marathon.objects.get(id = id )
    context = {
        "data": data
    } 
    return render(request, "community/community_marathon.html", context)


# 게시글 (검색 결과 표기)
# 페이지네이션 적용하기
def community_search(request):
    if request.method == "POST" :
        pass
    else : # get 으로 뭐 받아왔을때
        # 검색했을때 
        if request.GET.get("keyword"):
            keyword = request.GET.get("keyword")
            # 제목 또는 브랜드로 검색이 되야함
            datas = Post.objects.filter( Q(title__contains = keyword) | Q(content__contains = keyword) ).order_by("-pk")
        elif request.GET.get("category"):
            keyword = request.GET.get("category")
             # 자유 게시판 (category=1)
            if keyword == "all":
                datas = Post.objects.all()
            else: 
                datas = Post.objects.filter(category = keyword).order_by("-pk")
        # 검색안했을때
        else:
            keyword = 0
            datas = Post.objects.all()
        
    # 페이지네이션   
    page = request.GET.get("page") 
    paginator = Paginator(datas, 12) #10개씩보여주겠다
    rooms = paginator.get_page(page)   
        
    context = {
        "datas" : rooms,
        "keyword": keyword,
    }
    return render(request, "community/community_search.html", context)

# 댓글 쓰기  
@require_POST
def comments_create(request, id):
    # 어떤 게시물에 쓰는지 확인
    if request.user.is_authenticated :
        if request.method == "POST":
            comment_form = CommentForm(data = request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit = False)
                comment.author_id = request.user.id
                comment.save()
            else:
                print(comment_form.errors)

        return redirect("community:post_detail", id)
# 댓글 삭제    
def comment_delete(reqeust,id):
    delete_comment_data = Comment.objects.get(id=id)
    delete_comment_data.delete()
    return redirect("community:post_detail", id=delete_comment_data.post_id)

# 게시물에 좋아요 기능

# 좋아요 기능
def post_like(request, post_id):
    post = Post.objects.get(id = post_id) # 모델에서 데이터 꺼냄
    user = request.user # 사용자

    # 역참조해서
    if user.like_posts.filter(id = post.id).exists():
        # 좋아요 관계 삭제
        user.like_posts.remove(post) 
    else:
        user.like_posts.add(post) # 다대다관계에서 관계를 추가할땐!!!!! adddddddddddd

    # next 라는 값으로 전달되었다면 해당 위치로, 아니면 피드페이지로~ 분기 처리
    return redirect("community:post_detail", id=post_id)