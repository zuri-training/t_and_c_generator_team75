from django.urls import path
from .views import HomePageView, FeedbackPageView, DashboardPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("feedback/", FeedbackPageView.as_view(), name="feedback"),
    path("dashboard/", DashboardPageView.as_view(), name="dashboard"),
]
