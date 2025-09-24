import os
import urllib
from PIL import Image
from io import BytesIO
from django.contrib import messages
from urllib.request import urlopen
from django.shortcuts import redirect, render
from django.urls import reverse
from users.models import User
from home.models import Order, Shoe, Review, Cart, OrderItem
from django.db.models import Q # 모델의 데이터를 불러올때 조건값을 붙이기 위함 
from bs4 import BeautifulSoup
import requests

# Create your views here.
# 몰 메인
def mall_main(request):
    products = Shoe.objects.all()[:5] # 5개만 보여주기
    reviews = Review.objects.all()[:5]
    context = {
        "products" : products,
        "reviews" : reviews
    }
    return render(request, "mall/index.html", context)

# 상품 (검색 결과 표기)
def mall_product(request):
    if request.method == "POST" :
        pass
    else : # get 으로 뭐 받아왔을때
        # 검색했을때 
        if request.GET.get("keyword"):
            keyword = request.GET.get("keyword")
            # 제목 또는 브랜드로 검색이 되야함
            datas = Shoe.objects.filter( Q(name__contains = keyword) | Q(brand__name__contains = keyword) ).order_by("-pk")
            # 검색안했을때
        else:
            datas = Shoe.objects.all()
    context = {
        "datas" : datas,
    }
    return render(request, "mall/product.html", context)

# 상품상세
def mall_product_detail(request, id):
    data = Shoe.objects.get(id=id)
    context = {
        "data" : data,
    }
    return render(request, "mall/product_detail.html", context)

# 상품장바구니
def mall_cart(request):
    # user 정보를 불러온다.
    conn_user = request.user
    # user 의 장바구니 정보를 불러온다.
    # 유저아이디를 유저이름으로 찾는 행위가 맞는가...?
    user_id = User.objects.get(username=conn_user).id
    cart_datas = Cart.objects.filter(user_id=user_id)

    context = {
        "cart_datas" : cart_datas,
    }

    if request.method == "POST" :
        # 살 shoe_id 의 배열을 같이 보낸다.
        ids = request.POST.getlist("shoe_id[]")
        # 장바구니에 담았던 shoe_id 중 선택한 애들만 결제페이지로 보냄
        # get 으로 받으렴
        return redirect(reverse('parchase') + f'?id[]={ids}')

    return render(request, "mall/cart.html", context)

# 장바구니 추가
def mall_cart_add(request):
    if request.method == "POST":

        user = request.user # user 모델 변경시 변경해야함!!!!
        shoe_id = request.POST["shoe_id"]
        size = request.POST["size"]
        quantity = request.POST["quantity"]

        # 같은 유저에 같은 상품에 같은 
        exist_data = Cart.objects.filter(shoe_id=shoe_id, size=size, user_id=user)
      
        if exist_data.exists():
            print("장바구니에 넣을것이다")
            messages.warning(request, '이미 장바구니에 있습니다.')
            return redirect("product_detail", id=shoe_id)
        else: 
            print("장바구니에 넣을것이다")
            add_cart_data = Cart.objects.create(
                user = user,
                shoe = Shoe(id=shoe_id),
                size = size,
                quantity = quantity, 
            )

            print(user,shoe_id,size,quantity)
            add_cart_data.save()
            return redirect("cart") # 일단 장바구니로 가게함 
        #return redirect("product_detail", id=shoe_id ) # 계속보던 상품디테일 페이지로 다시 돌림

# 장바구니 삭제
def mall_cart_remove(request):
    pass

# 상품결제
def mall_parchase(request):
    # 결제를 요청
    if request.method == "POST":
        # 받을것 
        print(request.POST)
        result = request.POST
        # user 정보 user 없으면 날려버리는 거 안함
        conn_user = request.user
        
        name = result["name"]
        addr_num = result["addr_num"]
        address = result["address"]
        detail_address = result["detail_address"]
        phone = result["phone"]
        order_message = result["order_message"]
        # 배열값으로 나올것이여
        shoe_ids = result.getlist("shoe_id[]")
        prices = result.getlist("price[]") 
        shoe_sizes = result.getlist("shoe_size[]")
        quantitys = result.getlist("quantity[]")
        total_price = result["total_price"]
        pay_method = result["pay_method"]
        # Order model 에는 주문만 들어가게하기 => 한개 들어감 =======================

        order =  Order.objects.create(
            user = conn_user, # 내정보
            total_price = total_price,
            name = name, 
            phone = phone, 
            addr_num = addr_num,
            address = address,
            detail_address = detail_address,
            order_message = order_message,
            pay_method = pay_method, # 1번 무통장입금 2번 네이버페이
        )

        # OrderItem model 에는 상품별로 들어가게하기 => 여러개 들어감 =======================
        # 방금 주문한 Order 데이터 중 로그인한 사람의 id 와 가지고 맨 나중에 추가된 1개만
        order_id = Order.objects.filter(user = conn_user).last()
       
        # zip 을 이용해서 데이터를 엮어보자 
        orderItem = []
        for idx in range(len(shoe_ids)):
            orderItem.append(OrderItem(
                                order = Order(id=order_id.id),
                                shoe = Shoe(id=int(shoe_ids[idx])),
                                size = shoe_sizes[idx],
                                quantity = int(quantitys[idx]),
                                price = int(prices[idx]),
                            ))
        # 주문내역 저장
        if orderItem:
            OrderItem.objects.bulk_create(orderItem , batch_size=None, ignore_conflicts=False)
        
        # 주문서 1개 저장
        order.save()
        # Order 의 id 를 넘겨야함 # 구매정보를 알수있도록
        return redirect("parchase_completed") # 구매완료페이지로 넘기기 
    
    ids = eval(request.GET["id[]"]) # 아 개웃기다
    # 로그인한 계정의 장바구니에서 선택한 값을 가져온다
    cart_datas = Cart.objects.filter(id__in = ids)

    context = {
        "cart_datas" : cart_datas,
    }
    return render(request, "mall/parchase.html", context)

# 상품결제 취소 (실제 삭제할것인가...)
def mall_parchase_cancle(request):
    pass
# 삼품구매완료
def mall_parchase_completed(request):
    return render(request, "mall/parchase_completed.html")


















# 슈마커에서 데이터 크롤링해오기

# 1. https://www.shoemarker.co.kr/ASP/Product/SearchProductList.asp?SearchWord=%EB%9F%B0%EB%8B%9D%ED%99%94'
# 2. 위의 주소에서 크롤링을 진행한다.
# 3. 이름, 가격, 브랜드, 사진, 찜
# 4. .ly-img 안에 있는 a 태그의 href 에 접근한다. ( click ) 
# => 뽑아온 a 태그의 href 값을 for문을 돌려야하나?
# 5. .PhotoThumbnailProductScore__average_score_text 에서 별점을 얻는다.
# 6. 뒤로가기는 존재하지 않으므로 다시 접속을 한다? 


# 넣을 모델을 아직 설정하지 않았으므로 ExampeProduct 모델을 이용하겠다.
def crawling_shoes_page(request):
    # 슈마커 런닝화 검색
    url = "https://www.shoemarker.co.kr/ASP/Product/SearchProductList.asp?SearchType=C&SCode1=&SCode2=&SCode3=&SSort=&Page=2&SearchWord=%EB%9F%B0%EB%8B%9D%ED%99%94"

    header  = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US,en;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.google.com/",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }
    
    response = requests.get(url, headers=header)
    
    if response.status_code == 200: 
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 상품이름
        names = soup.select(".product-list .ly-name") # | 이거 기준을 split 해서 [0] 값 가져오는 처리
        # 상품 브랜드
        brands = soup.select(".product-list .ly-brand")
        # 상품 사진 url ()
        image_urls = soup.select(".product-list .ly-img img")
        links = soup.select(".product-list .ly-img img")
        prices = soup.select(".product-list .ly-price span:nth-child(1)") # 할인율을 안가져올것임
        # source_url = models.TextField() 
        # categories = models.ManyToManyField(Category) 
        # weight = models.IntegerField(null=True, blank=True) 
        # stock = models.IntegerField(default=0) 
        # rating = models.FloatField(default=0) 
        # created_at = models.DateTimeField(auto_now_add=True) 
        
        
        # 생각할점 ----------------------------------------------------
        # 브랜드는 Product 테이블과 ExampleBrand forienkey 로 연결되므로
        # 크롤링시 Brand 모델에서도 name 이 unique key 가 되어야하고 
        # Brand 모델에 brand 값이 없을때는 create 해서 추가하는 작업이 필요
        
        
        brand_arr = []
        image_url_arr = []
        link_arr = []
        price_arr = []
        name_arr = []
        
        originalUrl = 'https://www.shoemarker.co.kr'
        
        # zip 을 이용해서 데이터를 엮어보자 
        for brand, image_url, link, price, name in zip(brands,image_urls,links,prices,names):
            # brand
            brand_arr.append(brand.get_text().strip())
            # image_url
            image_url_arr.append(originalUrl + image_url["src"])
            # print(image_url["src"])
            #  # link
            # print(link)
            #  # price
            # print(price.get_text())
            # name
            name_arr.append(name.get_text().split("|")[0].strip())
            # new_shoes_datas.append(ExampleProduct(
            #                         name = name.text,
            #                         brand = brand.text,
            #                         ))
        
        # 이미지를 직접 저장할경우
        # 코드 가져온곳 : (https://dev-guardy.tistory.com/102)
        
        # save_folder = "images"
        # images 폴더가 없으면 만들어라
        # if not os.path.exists(save_folder):
        #     os.makedirs(save_folder)
        
        # for index, img_url  in enumerate(image_url_arr):
        #     img_response = requests.get(img_url)
        #     img = Image.open(BytesIO(img_response.content))
        #     img_name = os.path.join(save_folder, str(index) + '.png')
        #     img.save(img_name)
        #     print(f"Saved image: {img_name} (Height: {img.height})")
        
        # 이 기능을 필요없다~! # 이미지 직접저장시 그 파일을 어디에 처리할것인가
        # save_folder = "./images"
        # if not os.path.exists(save_folder):
        #     os.makedirs(save_folder)
        # print("image_url_arr")
        # print(image_url_arr)
        # for idx, i in enumerate(image_url_arr):
        #     # 이미지 요청 및 다운로드
        #     file_name = save_folder + "/" + str(idx) + ".jpg"
        #     urllib.request.urlretrieve(i, file_name)
        
        

        print(link_arr)            
        print(price_arr)  
        
        
                 
                  
        # if new_shoes_datas:
        #     # 여러개의 데이터값을..넣으려고...해봤다...
        #     ExampleProduct.objects.bulk_create(ExampleProduct, 
        #                                        batch_size=None, 
        #                                        ignore_conflicts=False)
        
    return redirect("mall_main")
    