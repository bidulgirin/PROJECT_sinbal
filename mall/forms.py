from django import forms
from mall.models import MallReview

class MallReviewForm(forms.ModelForm):
    class Meta:
        model = MallReview
        fields = [
          'title',
          'content',
          #'rating',
        ]

        labels = {
            "title" : "제목",
            "content" : "내용",
        }

        widgets = {
            "content": forms.Textarea(
                attrs = {
                    "class" : "form-control",
                    "placeholder":"내용",
                }
            ),
            "title" : forms.TextInput(
                attrs={
                    "class" : "form-control",
                    "placeholder":"제목",
                }
            )
        }

