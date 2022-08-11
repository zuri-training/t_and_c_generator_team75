from django.urls import path
from .views import HomePageView, FeedbackPageView, DashboardPageView, PrivacyDashboardPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("feedback/", FeedbackPageView.as_view(), name="feedback"),
    path("dashboard/", DashboardPageView.as_view(), name="dashboard"),
    path("privacypolicydashboard/", PrivacyDashboardPageView.as_view(), name="privacypolicydashboard"),
    
]
