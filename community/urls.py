from django.urls import path
from community import views 

urlpatterns = [
    path("", views.community, name = "community"),
    path("post/", views.add_post, name = "add_post"),
]