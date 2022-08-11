from django import forms
from accounts.models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
         'type':"text",
         'class':"Signup_Fields",
          'name':"username",
            'placeholder':"Enter your full name",
            'required' :'',
        })
        self.fields['email'].widget.attrs.update({
         'type':"email",
          'class':"Signup_Fields",
           'name':"email",
            'placeholder':"example@email.com",
          'required':''
        })
        self.fields['password'].widget.attrs.update({
        'type':"password", 'id':"password",
        'class':"Signup_Fields",
         'name':"password",
        'placeholder':"Enter your password",
         'minlength':"8",
          'required':''
        })
        

    class Meta:
        model = CustomUser
        fields = ['first_name','email','password']