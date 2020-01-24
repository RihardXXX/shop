from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    """Класс описывающий модели формы"""
    class Meta:
        model = Comment
        fields = ("text", )