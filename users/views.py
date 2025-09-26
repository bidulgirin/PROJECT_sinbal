from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib import auth
from django.urls import reverse
from users.forms import SignupForm, LoginForm

def login(request):
    # 이미 로그인되어 있다면
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        # LoginForm 객체를 만들며, 입력 데이터는 request.POST를 사용
        form = LoginForm(data = request.POST)
        
        # LoginForm에 전달된 데이터가 유효하다면
        if form.is_valid():
            # uesrname과 password값을 가져와 변수에 할당
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            
            # username, password에 해당하는 사용자가 있는지 검사
            user = authenticate(request, email=email, password=password)
            
            if user:
                auth_login(request, user)
                return redirect("/")
            else:
                form.add_error(None, "입력한 ID 혹은 PASSWORD에 해당하는 사용자가 없습니다")
        
        else:
            print(form.errors)
    else:
        # LoginForm 객체 생성
        form = LoginForm()
        
        # 생성한 LoginForm 객체를 템플릿에 "form"이라는 key로 전달
    context = {"form" : form}

    return render(request, "users/login.html", context)

def signup(request):
    
    if request.method == 'POST':
        form = SignupForm(data = request.POST)
        
        if form.is_valid():
            print("테스트2")
            user = form.save()
            auth_login(request, user)
            # 홈으로
            return redirect("home")
        else:
            print(form.errors)
    
    form = SignupForm()
    context = {"form" : form}
    return render(request, 'users/signup.html', context)

def logout(request):
    auth.logout(request)
    return redirect("/")
            
    
    