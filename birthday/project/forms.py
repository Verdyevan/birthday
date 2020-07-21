from django import forms
from .models import Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control mb-30',
        'id': 'message',
        'placeholder': 'Bisa comment loh',
        'cols': '30',
        'rows': '6'
    }))

    class Meta:
        model = Comment
        fields =('content', )

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']