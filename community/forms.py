# community/forms.py
from django import forms
from community.models import Post, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
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