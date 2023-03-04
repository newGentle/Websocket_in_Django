from allauth.account.forms import SignupForm

from django import forms


class CustomSignUpForm(SignupForm):
    username = forms.CharField(label='Имя Пользователя', max_length=64,min_length=3)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()
    
    def save(self, request):
        user = super().save(request)
        return user
