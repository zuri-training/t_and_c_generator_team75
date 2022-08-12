from django.db import models
from accounts.models import CustomUser

# Create your models here.

from django.db import models
# Create your models here.

class PolicyPost(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type_form = models.CharField(max_length = 10,default='Policies')

    is_website = models.BooleanField("Website",default=False)
    is_application = models.BooleanField("Application",default=False)

    app_name = models.CharField(max_length=200)
    companyURL = models.CharField(max_length=200)
    location =  models.CharField(max_length=200)
    policy_date = models.DateField()
   
    is_email_collected = models.BooleanField("Email Address",default=False)
    is_first_name_collected = models.BooleanField("First name and last name",default=False)
    is_phonenumber_collected = models.BooleanField("Phone number",default=False)
    is_address_collected = models.BooleanField("Address, state, city, zip/postal code",default=False)
    is_social_collected = models.BooleanField("Social medial profile information",default=False)
    is_others_collected = models.BooleanField("Others",default=False)
    your_other_collected = models.CharField(max_length=200,blank=True, default='')

    analytic = models.CharField(max_length=100)
    email_to_user = models.CharField(max_length=100)
    display_ads = models.CharField(max_length=100)
    pay_for_service= models.CharField(max_length=100)
    collect_information_from_kids = models.CharField(max_length=100)

    is_email_contacted = models.BooleanField("Email Address",default=False)
    is_website_contacted = models.BooleanField("A page on our website",default=False)
    is_phone_contacted = models.BooleanField(" Phone num",default=False)
    is_post_mail_contected = models.BooleanField("Sending post mail",default=False)

    is_i_agree = models.BooleanField("I agree to the Policify Terms and Conditions and Privacy Policy",default=False,blank=False)
    is_notify_me = models.BooleanField("Notify me of Policify policy updates.",default=False)

    def __str__(self):
        return self.app_name + "\n" + self.companyURL
    



class TermPost(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    type_form = models.CharField(max_length = 10, default='Terms')
    is_website = models.BooleanField("Website",default=False, null=False)
    is_application = models.BooleanField("Application",default=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    app_name = models.CharField(max_length=200)
    companyURL = models.CharField(max_length=200)
    location =  models.CharField(max_length=200)
    policy_date = models.DateField()

    create_account = models.CharField(max_length=100)
    upload_content = models.CharField(max_length=100)
    in_app_purchases = models.CharField(max_length=100)
    display_ads = models.CharField(max_length=100)
    buy_goods= models.CharField(max_length=100)
    subscription_plans = models.CharField(max_length=100)
    exclusive = models.CharField(max_length=100)

    is_email_contacted = models.BooleanField("Email Address",default=False, null=False)
    is_website_contacted = models.BooleanField("A page on our website",default=False, null=False)
    is_phone_contacted = models.BooleanField(" Phone num",default=False, null=False)
    is_post_mail_contected = models.BooleanField("Sending post mail",default=False, null=False)

    is_i_agree = models.BooleanField("I agree to the Policify Terms and Conditions and Privacy Policy",default=False,blank=False, null=False)
    is_notify_me = models.BooleanField("Notify me of Policify policy updates.",default=False, null=False)
    

    def __str__(self):
        return self.app_name + "\n" + self.companyURL
    
    