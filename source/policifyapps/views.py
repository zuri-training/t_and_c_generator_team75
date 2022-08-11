from django.shortcuts import render
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