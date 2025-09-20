from django.shortcuts import render
from mall.models import Example

# Create your views here.
# 몰 메인
def mall_main(request):
    return render(request, "mall/index.html")

# 상품(모두보기,런닝화,구두...)
def mall_product(request, slug):
    datas = Example.objects.filter(slug=slug)
    context = {
        "datas" : datas,
        "category" : slug,
    }
    return render(request, "mall/product.html", context)

# 상품상세
def mall_product_detail(request, id):
    data = Example.objects.get(id=id)
    context = {
        "data" : data,
    }
    return render(request, "mall/product_detail.html", context)
# 상품결제
def mall_parchase(request):
    return render(request, "mall/parchase.html")
# 삼품구매완료
def mall_parchase_completed(request):
    return render(request, "mall/parchase_completed.html")