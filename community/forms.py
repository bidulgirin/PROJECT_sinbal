<<<<<<< HEAD
from django import forms
from community.models import Post, Comment

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

=======
# community/forms.py
from django import forms
from community.models import Post, Comment

>>>>>>> 8dc3d1c8fb218a47a4845206c1d760baceac2cae
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
<<<<<<< HEAD
            "post"
        ]

        widgets = {
            "content": forms.Textarea(
                attrs = {
                    "class" : "form-control",
                    "placeholder":"내용",
                }
            ),
        }
=======
            "post",
        ]
        widgets = {
            "content" : forms.Textarea(
                attrs = {"placeholder" : "댓글 달기..."},
            )
        }
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "content",
        ]
>>>>>>> 8dc3d1c8fb218a47a4845206c1d760baceac2cae
