from django.urls import path
from community import views

app_name = "community"

urlpatterns = [
    # 커뮤니티 메인
    path("", views.community, name = "community"),
    # 마라톤
    path("marathon/<int:id>/", views.marathon, name = "marathon"),
    # 커뮤니티 글쓰기
    path("post/", views.add_post, name = "add_post"),
    # 커뮤니티 글 수정하기
    path("post/<int:id>/", views.edit_post, name = "edit_post"),
    # 커뮤니티 글 삭제하기
    path("post/delete/<int:id>/", views.delete_post, name = "delete_post"),
    # 커뮤니티 상세페이지
    path("post_detail/<int:id>/", views.post_detail, name = "post_detail"),
    # 커뮤니티 검색 
    path("search/", views.community_search, name = "community_search"),
    # 댓글 추가
    path("post_detail/<int:id>/comment_add/", views.comments_create, name = "comments_create"),
    # 댓글 삭제
    path("post_detail/<int:id>/comment_remove/", views.comment_delete, name = "comment_delete"),
    # 좋아요 기능
    path("post_detail/<int:post_id>/like/", views.post_like, name="post_like")
]