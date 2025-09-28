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
    # 커뮤니티 글 상세페이지
    path("post/delete/<int:id>/", views.delete_post, name = "delete_post"),
    # 커뮤니티 상세페이지
    path("post_detail/<int:id>/", views.product_detail, name = "product_detail"),
]