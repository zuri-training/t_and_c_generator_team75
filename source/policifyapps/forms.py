from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(widget=forms.TextInput(
        attrs={ 'type':"email",'name':"email",'id':"email",'placeholder':"olescharlie@gmail.com",'required':'','autofocus':''}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'type':"password",
                    'name':"password",
                    'id':"password",
                    'placeholder':"Password",
                    'maxlength':"20",
                    'required':'',
                    'autofocus':''
        }
))

class SignUpForm(UserCreationForm):
     def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields["username"].widget.attrs.update({
        
       })

     class Meta:
        model = User
        fields = ['username' ,'email', 'password1', 'password2' ]