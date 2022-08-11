from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm, UsernameField

from django import forms


from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email','password')



class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {
                'type':"email",'name':"email",'id':"email",'placeholder':"olescharlie@gmail.com",'required':'','autofocus':''
            }
        )
        self.fields['password'].widget.attrs.update(
            {
                 'type':"password",
                    'name':"password",
                    'id':"password",
                    'placeholder':"Password",
                    'maxlength':"20",
                    'required':'',
                    'autofocus':''
            }
        )
   


# class RegistrationForm(UserCreationForm):
#     email  = forms.EmailField(required=True)

#     class Meta:
#         model = CustomUser
#         fields = ['first_name','email','password1','password2']