import random
from django.shortcuts import render, redirect
from home.models import Shoe, Category, Marathon
from community.models import Post
from mypage.models import WishList
from datetime import *
from django.utils import timezone
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager


# Create your views here.
def home(request):
    today = timezone.now().date()
    categorys = Category.objects.all()[:5]
    hot_shoes = Shoe.objects.all().order_by("-rating")[:6]
    # 자유 게시판 (category=1)
    free_post = Post.objects.filter(category = "free").order_by('-views')[:1]
    # 요청 게시판 (category=2)
    request_post = Post.objects.filter(category = "request").order_by('-views')[:1]
    # 신발리뷰 게시판 (category=3)
    review_post = Post.objects.filter(category = "review").order_by('-views')[:1]
    # 마라톤후기 게시판 (category=4)
    marathon_post = Post.objects.filter(category = "marathon").order_by('-views')[:1]
    # 마라톤
    marathons = Marathon.objects.all().order_by('-pk')[:3]
    
    # 추천기능
    # 위시리스트 혹은 좋아하는 브랜드가 입력되었을경우에 발동 (현재좋아하는브랜드컬럼이보이지않으므로걍 위시리스트에서가지고옴)
    recommend_list = []
    wishlist_data = WishList.objects.filter(user_id = request.user.id) 
    # wishlist_data 에서 나오는 shoe_id 를 모두 불러와서 random 돌림
    if len(wishlist_data) > 0:
        for i in wishlist_data:
            recommend_list.append(i.shoe_id)
        # 랜덤으로 하나 뽑는다
        random_item = random.choice(recommend_list)
        recommend_shoe = Shoe.objects.get(id=random_item)
        
    else :
        recommend_shoe = 0
        
    context = {
        "categorys": categorys,
        "hot_shoes": hot_shoes,
        "free_post" : free_post,
        "request_post" : request_post,
        "review_post" : review_post,
        "marathon_post" : marathon_post,
        "marathons" : marathons,
        "recommend_shoe" : recommend_shoe,
        }
        
    return render(request, "home/home.html", context)

# 마라톤 대회 더미데이터 끌어오기 
def marathon_dumy_data(request):
    # 슈마커 런닝화 검색
    url = "http://www.roadrun.co.kr/schedule/list.php"

    header  = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US,en;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.google.com/",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }

    # selenium 
    options = webdriver.ChromeOptions()

    # headless 옵션 설정
    options.add_argument('headless')
    options.add_argument("no-sandbox")

    # 브라우저 윈도우 사이즈
    options.add_argument('window-size=1920x1080')

    # 사람처럼 보이게 하는 옵션들
    options.add_argument("disable-gpu")   # 가속 사용 x
    options.add_argument("lang=ko_KR")    # 가짜 플러그인 탑재
    #options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 이름 설정

    # 크롬 드라이버 최신 버전 설정
    service = ChromeService(executable_path=ChromeDriverManager().install())

    # 드라이버 위치 경로 입력
    driver = webdriver.Chrome(service=service, options=options)
    #driver = webdriver.Chrome()

    driver.get(url)
    driver.implicitly_wait(10) 

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    new_datas = []
    print("soupsoupsoupsoup")
    print(soup)
    # 마라톤 대회명
    names = soup.select("table:nth-child(2) tbody a")
    # dates = soup.select("div.event-card-header:nth-child(1)")
    # locations = soup.select("div.event-card-header .location-text")
    # distances = soup.select("div.event-card-header .course-tag:nth-child(1)")
    # prices = soup.select("div.event-card-header table tr:nth-child(3) div:nth-child(1)")
    # website_urls = soup.select("div.event-card-header a")

    #names = driver.find_elements(By.CLASS_NAME, "h3")
    # dates = driver.find_elements("div.event-card-header:nth-child(1)")
    # locations = driver.find_elements("div.event-card-header .location-text")
    # distances = driver.find_elements("div.event-card-header .course-tag:nth-child(1)")
    # prices = driver.find_elements("div.event-card-header table tr:nth-child(3) div:nth-child(1)")
    # website_urls = driver.find_elements("div.event-card-header a")
    
    print("names")
    print(names)

    # print("dates")
    # print(dates)
    # print("locations")
    # print(locations)
    # print("distances")
    # print(distances)
    # print("prices")
    # print(prices)
    # print("website_urls")
    # print(website_urls)


    # zip 을 이용해서 데이터를 엮어보자 
    # for name,date,location,distance,price,website_url in zip(names,dates,locations,distances,prices,website_urls):
        
    #     new_datas.append(Marathon(
    #                             name = name.text,
    #                             date = date.text,
    #                             location = location.text,
    #                             distance = distance.text,
    #                             price = price.text,
    #                             website_url = website_url.text,
    #                             ))
    
    # if new_datas:
    #     # 여러개의 데이터값을..넣으려고...해봤다...
    #     Marathon.objects.bulk_create(new_datas, 
    #                             batch_size=None, 
    #                             ignore_conflicts=False)

    #driver.get_screenshot_as_file('capture_naver.png')    # 화면캡처
    driver.quit() # driver 종료    
    return redirect("home")



