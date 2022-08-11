from django.shortcuts import render, redirect
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name ="home.html"
    
class FeedbackPageView(TemplateView):
    template_name = "feedback.html"
    
class DashboardPageView(TemplateView):
    template_name = "dashboard/dashboard.html"
    
    
class PrivacyDashboardPageView(TemplateView):
    template_name = "dashboard/privpolicydash.html"





def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid:
        pass
    else:
        form = SignUpForm()
    context  = {
        "form": form
    }
    return render(request, 'registration/sign_up.html',context)

