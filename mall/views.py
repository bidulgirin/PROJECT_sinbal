from django.shortcuts import render

# Create your views here.
# 몰 메인
def mall_main(request):
    return render(request, "mall/index.html")
# 상품(모두보기,런닝화종류1,런닝화종류2)
def mall_product(request, category):
    context = {
        "category" : category
    }
    return render(request, "mall/product.html", context)
# 상품상세
def mall_product_detail(request, id):
    return render(request, "mall/product_detail.html")
# 상품결제
def mall_parchase(request):
    return render(request, "mall/parchase.html")
# 삼품구매완료
def mall_parchase_completed(request):
    return render(request, "mall/parchase_completed.html")