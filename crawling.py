import requests
from bs4 import BeautifulSoup
import os
# Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록한다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sinbal_pj.settings")
import django
# 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만든다.
django.setup()

from home.models import Brand, Shoe
# .area-pagination .page-num1
def shoes():
    brands = []
    names = []
    prices = []
    imges = []
    codes = []
    descriptions = []

    for i in range(7):
        url1 = requests.get("https://www.shoemarker.co.kr/ASP/Product/ProductList.asp?SearchType=S&SCode1=02&SCode2=01&SCode3=0"+str(1+i)+"&SSort=&Page=01&SPrice=0&EPrice=50")
        html1 = url1.content
        soup1 = BeautifulSoup(html1, 'lxml')
        for j in range(int(soup1.select_one(".page-num1 a").text)):
            url = requests.get("https://www.shoemarker.co.kr/ASP/Product/ProductList.asp?SearchType=S&SCode1=02&SCode2=01&SCode3=0"+str(1+i)+"&SSort=&Page="+str(1+j)+"&SPrice=0&EPrice=50")
            html = url.content.decode('utf-8','replace') # 한글이 깨져서 넣어주었다.
            soup = BeautifulSoup(html, 'lxml')
            for brand in soup.select(".product-list .ns-type-bl-eb13x"):
                brands.append(brand.text)

            for name in soup.select(".product-list .ns-type-bl-r a"):
                names.append(name.text)

            for price in soup.select(".product-list .ns-type-bl-eb18x"):
                if "품절" in price.text.strip():
                    prices.append(0)
                else:
                    prices.append(price.text.strip().replace(",", ""))

            for img in soup.select(".product-list .ly-img img"):
                imges.append(img.get("src", ""))

        #     for code in soup.select(".product-list div.ns-type-bl-r a"):
        #         codes.append(code.get("href", "").split("=")[1]) from fake_useragent import UserAgent
            
        # for c in codes:
        #     headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}
        #     url2 = requests.get("https://www.shoemarker.co.kr/ASP/Product/ProductDetail.asp?ProductCode="+str(c), headers=headers)
        #     html2 = url2.content.decode('utf-8','replace')
        #     soup2 = BeautifulSoup(html2, 'lxml')

        #     for description in soup2.select(".product-info-box .info-list li"):
        #         descriptions.append(description.text.strip().replace("\n", " = "), descriptions, shoes()[5], description = each_shoes[4]


    return brands, names, prices, imges, codes

shoes_list = set(shoes()[0])
for brand_list in shoes_list:
    brand_DB = Brand(name=brand_list)
    brand_DB.save()

for each_shoes in zip(shoes()[0], shoes()[1], shoes()[2], shoes()[3]):
    if Brand(name=each_shoes[0]):
        shoeshoe = Shoe(name=each_shoes[1], price=int(each_shoes[2]), images=each_shoes[3], brand_id = int(Brand.objects.get(name=each_shoes[0]).id))
        shoeshoe.save()
