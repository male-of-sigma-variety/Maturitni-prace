from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ["author_name", "comment", "ratings" ]

#class RawReviewFrom: