from django import forms
from mall.models import MallReview

class MallReviewForm(forms.ModelForm):
    class Meta:
        model = MallReview
        fields = [
          'title',
          'content',
          'rating',
        ]
        widgets = {
            "content": forms.Textarea(
                attrs = {
                    "placeholder":"발 볼 크기가 딱 맞아용... ",
                }
            )
        }

