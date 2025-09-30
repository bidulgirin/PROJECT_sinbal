from django.urls import path
from home import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("m/", views.marathon_dumy_data, name = "marathon_dumy_data"),
    
]