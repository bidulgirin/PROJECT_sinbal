from django import forms
from django.core.exceptions import ValidationError
from users.models import User, UserBio

# Create your forms here.

class SignupForm(forms.Form):
    profile_image = forms.ImageField(
        label = "프로필 이미지", 
        required = False
    )
    short_description = forms.CharField(
        label = "자기소개",
        max_length = 100,
        widget = forms.TextInput(
            attrs = {"class" : "form-control",
                     "placeholder" : "자신에 대해 알려주세요"}
        ),
        required = False
    )
    
    username = forms.CharField(
        label = "ID",
        min_length = 2,
        max_length = 6,
        widget = forms.TextInput(
            attrs = {"class" : "form-control",
                    "placeholder": "이름"}
            )
        )
    
    email = forms.EmailField(
        label = "이메일",
        widget=forms.EmailInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "이메일"}
            )
        )
    
    nickname = forms.CharField(
        label = "닉네임",
        min_length = 2,
        max_length = 8,
        required = True,
        widget = forms.TextInput(
            attrs = {"class" : "form-control",
                     "placeholder" : "ex)테토남"}
            )
        )
    
    password = forms.CharField(
        label = "비밀번호",
        min_length=8,
        max_length=16,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", 
                   "placeholder": "비밀번호"}
            )
        )
    
    password2 = forms.CharField(
        label = "비밀번호 확인",
        min_length=8,
        max_length=16,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", 
                   "placeholder": "비밀번호"}
            )
        )
    
    #* UserBio
    shoe_size = forms.IntegerField(
        label = "본인 사이즈",
        min_value = 200,
        max_value = 300,
        widget = forms.NumberInput(
            attrs={"class" : "form-control",
                   "placeholder" : "ex)260"}
        ),
        required = False
    )
    
    ball_foot = forms.ChoiceField(
        label = "발볼 크기",
        choices = UserBio.CATEGORY,
        widget = forms.RadioSelect(),
        required = False,
        initial="Regular"
    )
    
    favorite_brand = forms.CharField(
        label = "선호하는 브랜드 작성",
        max_length = 10,
        widget = forms.TextInput(
            attrs = {"class" : "form-control",
                     "placeholder" : "ex) 나이키, 아이다스"}
        ),
        required = False
    )
    
    address = forms.CharField(
        label = "상세주소",
        max_length = 100,
        widget = forms.TextInput(
            attrs = {"class" : "form-control",
                     "placeholder" : "상세주소를 입력하세요"}
        )
    )
    
    gender = forms.ChoiceField(
        label = "성별",
        choices = User.GENDER,
        widget = forms.RadioSelect(),
        required = False,
        initial = "Male"
    )
    
    def clean_nickname(self):
        print("테스트4")
        nickname = self.cleaned_data["nickname"]

        if User.objects.filter(nickname = nickname).exists():
            raise ValidationError(f"입력한 닉네임({nickname})은 이미 사용 중입니다")
        
        return nickname
    
    def clean_size(self):
        print("테스트5")
        size = self.cleaned_data.get("shoe_size")
        
        if size and size % 5 != 0:
            raise ValidationError("신발 사이즈는 5단위여야 합니다(250,255,260...)")
        
        return size
    
    def clean(self):
        print("테스트6")
        password = self.cleaned_data.get("password", None)
        password2 = self.cleaned_data.get("password2", None)

        if password != password2:
            # password2 필드에 오류를 추가
            # 위에 함수는 누구 오류인지 명확하니 add_error 를 따로 하지 않아도 됨
            self.add_error("password2", "비밀번호화 비밀번호 확인란의 값이 다릅니다")
            
        return self.cleaned_data

    def save(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        nickname = self.cleaned_data.get("nickname")
        profile_image = self.cleaned_data.get("image")
        short_description = self.cleaned_data.get("short_description")
        address = self.cleaned_data.get("address")
        gender = self.cleaned_data.get("gender")
        shoe_size = self.cleaned_data.get("shoe_size")
        ball_foot = self.cleaned_data.get("ball_foot")
        favorite_brand = self.cleaned_data.get("favorite_brand")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            nickname=nickname,
            gender=gender,
            address=address
        )
        
        if short_description:
            user.short_description = short_description
        if profile_image:
            user.profile_image = profile_image
        
        user.save()

        if shoe_size:
            user_bio = UserBio.objects.create(
                user=user,
                shoe_size=shoe_size,
                ball_foot=ball_foot,
                favorite_brand=favorite_brand
            )
            user_bio.save() #이거 없었음 

        return user

class LoginForm(forms.Form):
    email = forms.EmailField(min_length=4,
                            widget = forms.TextInput(
                            attrs = {"placeholder" : "ID",
                                    "class" : "form-control"}))
    
    password = forms.CharField(min_length = 4,
                               widget = forms.PasswordInput(
                                attrs = {"placeholder" : "PASSWORD",
                                        "class" : "form-control"}))