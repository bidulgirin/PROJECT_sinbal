# community/views.py
from django.shortcuts import render


def community(request):
    return render(request, "community/community.html")

def add_post(request):
    return render(request, "community/community_post.html")