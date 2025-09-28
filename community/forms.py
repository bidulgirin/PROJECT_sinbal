from django import forms
from community.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        
        model = Post
        fields = [
            "category", 
            "title", 
            "content"
                ]
        labels = {
            "category": "게시판 선택",
            "title": "제목",
            "content": "내용",
        }
        widgets = {
            "category": forms.Select(attrs={
                "class": "form-select"
                }),
            "title": forms.TextInput(attrs={
                "class": "form-control", 
                "placeholder": "제목을 입력하세요"
                }),
            "content": forms.Textarea(attrs={
                "class": "form-control", 
                "rows": 14, 
                "placeholder": "내용을 입력하세요"}),
        }

