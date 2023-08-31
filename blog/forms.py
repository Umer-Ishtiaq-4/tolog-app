from django.forms import ModelForm
from django import forms
from .models import TODO, Post
from django.contrib.auth.models import User



class TODOForm(ModelForm):
    
    
    class Meta:
        model = TODO
        fields = ['title' , 'status' , 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
        }
        

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            
        }
        

