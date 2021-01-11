from django import forms
from .models import Comment


class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'class': "form-control form-control-sm"}))
