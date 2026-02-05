from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titles', 'text', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название постп'
        }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': 'Текст поста'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control-file'
            })
        }

