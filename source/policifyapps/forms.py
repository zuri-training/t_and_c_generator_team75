from django import forms
from accounts.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from .models import PolicyPost ,TermPost

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
        self.fields['password1'].widget.attrs.update({
        'type':"password", 'id':"password",
        'class':"Signup_Fields",
         'name':"password",
        'placeholder':"Enter your password",
         'minlength':"8",
          'required':''
        })
        self.fields['password2'].widget.attrs.update({
        'type':"password", 'id':"password",
        'class':"Signup_Fields",
         'name':"password",
        'placeholder':"Enter your password again",
         'minlength':"8",
          'required':''
        })
        

    class Meta:
        model = CustomUser
        fields = ['first_name','email','password1','password2']


class PoliciesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        self.fields['is_website'].widget.attrs.update({
            'type':"checkbox", 'name':"user" ,'value':"website", 'class':"input-checkbox"
        })
        self.fields['is_application'].widget.attrs.update({
            'type':"checkbox" ,'name':"user", 'value':"application" ,'class':"input-checkbox"
        })
        self.fields['app_name'].widget.attrs.update({
            'type':"text", 'name':"policyenterprise" ,'placeholder':"My Company name", 'required':''
        })
        self.fields['companyURL'].widget.attrs.update({
         'type':"url", 'name':"policyurl", 'placeholder':"http://www.mycompanyname.com", 'required':''
        })
        self.fields['location'].widget.attrs.update({
         'type':"text", 'name':"policylocation", 'placeholder':"E.g Lagos/Nigeria", 'required':''
        })
        self.fields['policy_date'].widget.attrs.update({
         'type':"date", 'name':"policydate" ,'placeholder':"2022-08-17" ,'required':''
        })
        self.fields['is_email_collected'].widget.attrs.update({
         'type':"checkbox", 'name':"info", 'value':"email", 'class':"input-checkbox"
        })
        self.fields['is_first_name_collected'].widget.attrs.update({
         'type':"checkbox" ,'name':"info", 'value':"firstandlastname" ,'class':"input-checkbox"
        })
        self.fields['is_phonenumber_collected'].widget.attrs.update({
            'type':"checkbox", 'name':"info", 'value':"phone", 'class':"input-checkbox"
        })
        self.fields['is_address_collected'].widget.attrs.update({
         'type':"checkbox", 'name':"info", 'value':"address", 'class':"input-checkbox"
        })
        self.fields['is_social_collected'].widget.attrs.update({
         'type':"checkbox", 'name':"info", 'value':"socials", 'class':"input-checkbox"
        })
        self.fields['is_others_collected'].widget.attrs.update({
            'type':"checkbox" ,'name':"info", 'value':"others" ,'class':"input-checkbox"
        })
        self.fields['your_other_collected'].widget.attrs.update({
             'type':"text" ,'name':"add-other", 'placeholder':"Add Your Own"
        })
        self.fields['analytic'].widget.attrs.update({
         'type':"radio", 'name':"trackinfo",  'class':"input-radio"
        })
        self.fields['email_to_user'].widget.attrs.update({
            'type':"radio" ,'name':"emailinfo",  'class':"input-radio"
        })
        self.fields['display_ads'].widget.attrs.update({
            'type':"radio", 'name':"adinfo", 'value':"ads", 'class':"input-radio"
        })
        self.fields['pay_for_service'].widget.attrs.update({
            'type':"radio", 'name':"payinfo" ,'value':"pay" ,'class':"input-radio"
        })
        self.fields['collect_information_from_kids'].widget.attrs.update({
         'type':"radio", 'name':"kidinfo", 'value':"kid", 'class':"input-radio"
        })
        self.fields['is_email_contacted'].widget.attrs.update({
          'type':"checkbox", 'name':"user-contact" ,'value':"mail", 'class':"input-checkbox"
        })
        self.fields['is_website_contacted'].widget.attrs.update({
         'type':"checkbox", 'name':"user-contact", 'value':"web" ,'class':"input-checkbox"
        })
        self.fields['is_phone_contacted'].widget.attrs.update({
         'type':"checkbox", 'name':"user-contact", 'value':"phonenum", 'class':"input-checkbox"
        })
        self.fields['is_post_mail_contected'].widget.attrs.update({
         'type':"checkbox", 'name':"user-contact" ,'value':"postmail", 'class':"input-checkbox"
        })
        self.fields['is_i_agree'].widget.attrs.update({
         'type':"checkbox", 'name':"terminfo", 'value':"agree", 'class':"input-checkbox" , 'required':''
        })
        self.fields['is_notify_me'].widget.attrs.update({
         'type':"checkbox", 'name':"terminfo", 'value':"notify" ,'class':"input-checkbox"
        })

    
    anal_CHOICES = [('Yes, we use tracking or analytics tools','Yes, we use tracking or analytics tools'),(' No',' No')]
    analytic = forms.ChoiceField(required=True,widget=forms.RadioSelect, choices=anal_CHOICES)

    email_CHOICES =  [('Yes, we send emails to our users if subscribed to','Yes, we send emails to our users if subscribed to'),(' No',' No')]
    email_to_user = forms.ChoiceField(required=True,widget=forms.RadioSelect, choices=email_CHOICES)

    display_ad_CHOICES = [('Yes, we show ads','Yes, we show ads'),(' No',' No')]
    display_ads = forms.ChoiceField(required=True,widget=forms.RadioSelect, choices=display_ad_CHOICES)
    pay_for_CHOICES = [('Yes, users can pay for products and services on our website','Yes, users can pay for products and services on our website'),(' No',' No')]
    pay_for_service =forms.ChoiceField(required=True,widget=forms.RadioSelect, choices=pay_for_CHOICES)
    from_kids_CHOICES =[('Yes, we collect information from kids under the age of 13.','Yes, we collect information from kids under the age of 13.'),(' No',' No')]
    collect_information_from_kids = forms.ChoiceField(required=True,widget=forms.RadioSelect, choices=from_kids_CHOICES)
    is_notify_me = forms.BooleanField(required= True)
    class Meta:
        model = PolicyPost 
        fields = ['is_website',
                'is_application',
                'app_name',
                'companyURL',
                'location',
                'policy_date',
                'is_email_collected',
                'is_first_name_collected',
                'is_phonenumber_collected',
                'is_address_collected',
                'is_social_collected',
                'is_others_collected',
                'your_other_collected',
                'analytic',
                'email_to_user',
                'display_ads',
                'pay_for_service',
                'collect_information_from_kids',
                'is_email_contacted',
                'is_website_contacted',
                'is_phone_contacted',
                'is_post_mail_contected',
                'is_i_agree',
                'is_notify_me',]


class TermsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        self.fields['is_website'].widget.attrs.update({
            'type':"checkbox", 'name':"user" ,'value':"website", 'class':"input-checkbox"
        })
        self.fields['is_application'].widget.attrs.update({
            'type':"checkbox" ,'name':"user", 'value':"application" ,'class':"input-checkbox"
        })
        self.fields['app_name'].widget.attrs.update({
            'type':"text", 'name':"policyenterprise" ,'placeholder':"My Company name", 'required':''
        })
        self.fields['companyURL'].widget.attrs.update({
         'type':"url", 'name':"policyurl", 'placeholder':"http://www.mycompanyname.com", 'required':''
        })
        self.fields['location'].widget.attrs.update({
         'type':"text", 'name':"policylocation", 'placeholder':"E.g Lagos/Nigeria", 'required':''
        })
        self.fields['policy_date'].widget.attrs.update({
         'type':"date", 'name':"policydate" ,'placeholder':"2022-08-17" ,'required':''
        })
        
        self.fields['create_account'].widget.attrs.update({
         'type':"radio", 'name':"user-account",  'class':"input-radio"
        })
        self.fields['upload_content'].widget.attrs.update({
         'type':"radio", 'name':"user-content",  'class':"input-radio"
        })
        self.fields['in_app_purchases'].widget.attrs.update({
            'type':"radio" ,'name':"user-purchase",  'class':"input-radio"
        })
        self.fields['display_ads'].widget.attrs.update({
            'type':"radio", 'name':"ads", 'class':"input-radio"
        })
        self.fields['buy_goods'].widget.attrs.update({
            'type':"radio", 'name':"user-buy"  ,'class':"input-radio"
        })
        self.fields['subscription_plans'].widget.attrs.update({
         'type':"radio", 'name':"user-sub",  'class':"input-radio"
        })
        self.fields['exclusive'].widget.attrs.update({
         'type':"radio", 'name':"trademark",  'class':"input-radio"
        })
        self.fields['is_email_contacted'].widget.attrs.update({
          'type':"checkbox", 'name':"user-contact" ,'value':"mail", 'class':"input-checkbox"
        })
        self.fields['is_website_contacted'].widget.attrs.update({
         'type':"checkbox", 'name':"user-contact", 'value':"web" ,'class':"input-checkbox"
        })
        self.fields['is_phone_contacted'].widget.attrs.update({
         'type':"checkbox", 'name':"user-contact", 'value':"phonenum", 'class':"input-checkbox"
        })
        self.fields['is_post_mail_contected'].widget.attrs.update({
         'type':"checkbox", 'name':"user-contact" ,'value':"postmail", 'class':"input-checkbox"
        })
        self.fields['is_i_agree'].widget.attrs.update({
         'type':"checkbox", 'name':"terminfo", 'value':"agree", 'class':"input-checkbox" , 'required':''
        })
        self.fields['is_notify_me'].widget.attrs.update({
         'type':"checkbox", 'name':"terminfo", 'value':"notify" ,'class':"input-checkbox"
        })

    create_account_CHOICES = [('Yes, users can create account','Yes, users can create account'),(' No',' No')]
    create_account = forms.ChoiceField(required=True,widget=forms.RadioSelect, choices=create_account_CHOICES)
    upload_CHOICES = [('Yes, users can create and/or upload content','Yes, users can create and/or upload content'),(' No',' No')]
    upload_content = forms.ChoiceField(required=True,widget=forms.RadioSelect, choices=upload_CHOICES)
    in_app_CHOICES = [('Yes, we offer website/in-app purchases?','Yes, we offer website/in-app purchases?'),(' No',' No')]
    in_app_purchases = forms.ChoiceField(required=True,widget=forms.RadioSelect, choices=in_app_CHOICES)
    display_add_CHOICES = [('Yes, we show ads','  Yes, we show ads'),(' No',' No')]
    display_ads = forms.ChoiceField(required=True,widget=forms.RadioSelect, choices=display_add_CHOICES)
    subscription_CHOICES = [('Yes, user can pay Subscription',' Yes, user can pay Subscription'),(' No',' No')]
    subscription_plans = forms.ChoiceField(required=True,widget=forms.RadioSelect, choices=subscription_CHOICES)
    buy_goods_CHOICES = [('Yes, user can buy goods','Yes, user can buy goods'),(' No',' No')]
    buy_goods = forms.ChoiceField(required=True,widget=forms.RadioSelect, choices=buy_goods_CHOICES)
    exclusive_CHOICES = [('Yes, our content (logo and trademarks) is our exclusive property','Yes, our content (logo and trademarks) is our exclusive property'),(' No',' No')]
    exclusive = forms.ChoiceField(required=True,widget=forms.RadioSelect, choices=exclusive_CHOICES)
    is_notify_me = forms.BooleanField(required= True)
    class Meta:
        model = TermPost 
        fields = ['is_website',
                'is_application',
                'app_name',
                'companyURL',
                'location',
                'policy_date',
                'create_account',
                'upload_content',
                'in_app_purchases',
                'display_ads',
                'buy_goods',
                'subscription_plans',
                'exclusive',
                'is_email_contacted',
                'is_website_contacted',
                'is_phone_contacted',
                'is_post_mail_contected',
                'is_i_agree',
                'is_notify_me',
    ]