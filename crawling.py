import requests
from bs4 import BeautifulSoup
import os
# Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록한다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sinbal_pj.settings")
import django
# 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만든다.
django.setup()

from home.models import Brand, Shoe

def shoes():
    brands = []
    names = []
    prices = []
    imges = []

    url1 = requests.get("https://www.shoemarker.co.kr/ASP/Product/ProductList.asp?SCode1=02&SCode2=01&SCode3=01")
    html = url1.content
    soup1 = BeautifulSoup(html, 'lxml')
    for i in range(int(soup1.select(".page-num1 > a")[0].text)):
        url = requests.get("https://www.shoemarker.co.kr/ASP/Product/ProductList.asp?SearchType=S&SCode1=02&SCode2=01&SCode3=01&SSort=&Page="+str(1+i)+"&SPrice=0&EPrice=50")
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
    return brands, names, prices, imges


a = set(shoes()[0])
for b in a:
    c = Brand(name=b)
    c.save()


for a in zip(shoes()[0], shoes()[1], shoes()[2], shoes()[3]):
    if Brand(name=str(a[0])):
        c = Shoe(brand=Brand(name=str(a[0])).id, name=a[1], price=int(a[2]), images=a[3])
        c.save
