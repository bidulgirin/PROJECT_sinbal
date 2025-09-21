import os
import urllib
from PIL import Image
from io import BytesIO
from urllib.request import urlopen
from django.shortcuts import redirect, render
from mall.models import Example, ExampleProduct
from bs4 import BeautifulSoup
import requests

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
        
        save_folder = "./images"
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
        print("image_url_arr")
        print(image_url_arr)
        for idx, i in enumerate(image_url_arr):
            # 이미지 요청 및 다운로드
            file_name = save_folder + "/" + str(idx) + ".jpg"
            urllib.request.urlretrieve(i, file_name)
        
        

        print(link_arr)            
        print(price_arr)  
        
        
                 
                  
        # if new_shoes_datas:
        #     # 여러개의 데이터값을..넣으려고...해봤다...
        #     ExampleProduct.objects.bulk_create(ExampleProduct, 
        #                                        batch_size=None, 
        #                                        ignore_conflicts=False)
        
    return redirect("mall_main")
    