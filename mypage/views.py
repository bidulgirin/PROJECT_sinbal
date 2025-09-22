from django.shortcuts import render

# Create your views here.
def MainMypage(request):
    return render(request, "my_main.html")