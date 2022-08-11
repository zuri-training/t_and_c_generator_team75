from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from . forms import RegistrationForm
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
    


# Create your views here.
class HomePageView(TemplateView):
    template_name ="home.html"
    
class FeedbackPageView(TemplateView):
    template_name = "feedback.html"
    
class DashboardPageView(TemplateView):
    template_name = "dashboard.html"

