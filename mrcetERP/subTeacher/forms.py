from subTeacher.models import STsignin,STLogIn
from django import forms

class SigninForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model=STsignin
        fields='__all__'
class LoginForm(forms.ModelForm):
    user_password= forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=STLogIn
        fields='__all__'