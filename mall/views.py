from django.shortcuts import render

# Create your views here.
def mall_main(request):
    return render(request, "mall/index.html")