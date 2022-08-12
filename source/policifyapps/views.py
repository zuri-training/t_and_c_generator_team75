from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from . forms import RegistrationForm , PoliciesForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def sign_up(request):
     if request.method == 'POST':
          form = RegistrationForm(request.POST)
          print(form)
          if form.is_valid():
               user = form.save()
               login(request,user)
               return redirect('/home')
     else:
          form = RegistrationForm()
     return render(request,'registration/sign_up.html',{'form':form})
    


class HomePageView(TemplateView):
    template_name ="home.html"
    
class FeedbackPageView(TemplateView):
    template_name = "feedback.html"

 
class DashboardPageView(TemplateView):
    login_required = True
    template_name = "dashboard/dashboard.html"
    
    
class PrivacyDashboardPageView(TemplateView):
    login_required = True
    template_name = "dashboard/privpolicydash.html"


class TermsDashboardPageView(TemplateView):
    login_required = True
    template_name = "dashboard/termscondash.html"
    
class PolicyPreviewPage(TemplateView):
    template_name = "dashboard/policypreview.html"

#@login_required(login_url="/login")
def create_policiy_post(request):
    if request.method == 'POST':
        form = PoliciesForm(request.POST)
        if form.is_valid():
            post = form.save(commit= False)
            post.author = request.user
            print(post.author)
            post.save()
            return redirect('/home')
    else:
        form = PoliciesForm()

    return render(request, 'dashboard/privpolicydash.html',{"form" : form})





#delete this if you are not using anymore it keeps giving me issues
    #
      #def signup(request):
    #form = SignUpForm(request.POST)
    #if form.is_valid:
        #pass
    #else:
        #form = SignUpForm()
    #context  = {
        #"form": form
    #}
    #return render(request, 'registration/sign_up.html',context)

  
   
