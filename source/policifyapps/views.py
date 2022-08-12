from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from . forms import RegistrationForm , PoliciesForm , TermsForm
from django.contrib.auth.decorators import login_required
from .models import PolicyPost, TermPost

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
    template_name = "dashboard/dashboard.html"
    
    
class PrivacyDashboardPageView(TemplateView):
    template_name = "dashboard/privpolicydash.html"


class TermsDashboardPageView(TemplateView):
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
            return redirect('/dashboard')
    else:
        form = PoliciesForm()

    return render(request, 'dashboard/privpolicydash.html',{"form" : form})

def create_terms_post(request):
    if request.method == 'POST':
        form = TermsForm(request.POST)
        if form.is_valid():
            post = form.save(commit= False)
            post.author = request.user
            print(post.author)
            post.save()
            return redirect('/dashboard')
    else:
        form = TermsForm()

    return render(request, 'dashboard/termscondash.html',{"form" : form})


def all_post(request):
     posts = PolicyPost.objects.all()
     terms = TermPost.objects.all()
     context = {
        "posts":posts,
        "terms":terms,
     }
     if request.method == "POST":
          post_id = request.POST.get("post-id")
          edit_id = request.POST.get("edit-id")
          if post_id:
               post = PolicyPost.objects.filter(id=post_id).first()
               if post and post.author == request.user:
                    post.delete()
          elif edit_id:
               return redirect(f'/edit-post/{edit_id}')
               
     return render(request,"dashboard/dashboard.html",context)

  
   
