from django import forms
from .models import Post,Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','text',)
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 20}),  # Customize cols and rows as needed
            'title': forms.Textarea(attrs={'cols': 80 , 'rows':1}),  # Customize cols and rows as needed
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author','text',)