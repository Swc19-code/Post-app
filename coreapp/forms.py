from . models import Blog
from django import forms

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = 'title', 'category', 'image', 'content'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
        }
