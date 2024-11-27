from cProfile import label

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms




class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label='نام',
        max_length=40,
        widget=forms.TextInput(
            attrs={'class': 'form-control' , 'placeholder':'نام خود را وارد کنید' }
        )
    )
    last_name = forms.CharField(
        label='نام خانوادگی',
        max_length=40,
        widget=forms.TextInput(
            attrs={'class': 'form-control' , 'placeholder':'نام خانوادگی خود را وارد کنید' }
        )
    )
    
    email = forms.EmailField(
        label='ایمیل',
        max_length=60,
        widget=forms.TextInput(
            attrs={'class': 'form-control' , 'placeholder':'ایمیل خود را وارد کنید' }
        )
    )
    username = forms.CharField(
        label='نام کاربری',
        max_length=50,
        widget=forms.TextInput(
            attrs={'class': 'form-control' , 'placeholder':'نام کاربری خود را وارد کنید' }
        )
    )

    password1 = forms.CharField(
        label="رمز",
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label="تکرار رمز",
        widget=forms.PasswordInput()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'name': 'password',
            'type': 'password',
            'placeholder': 'رمز باید بالای 8 کاراکتر باشد',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'name': 'password2',
            'type': 'password',
            'placeholder': 'رمز خود را تکرار کنید',
        })


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
