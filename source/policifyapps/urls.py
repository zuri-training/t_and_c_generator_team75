from django.urls import path
from .views import HomePageView, FeedbackPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("feedback/", FeedbackPageView.as_view(), name="feedback"),
]
