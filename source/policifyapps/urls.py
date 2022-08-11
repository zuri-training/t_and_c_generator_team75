from django.urls import path
from .views import HomePageView, FeedbackPageView, DashboardPageView
from django.contrib.auth import views
from .views import sign_up

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
     path("home", HomePageView.as_view(), name="home"),
    path("feedback/", FeedbackPageView.as_view(), name="feedback"),
    path("dashboard/", DashboardPageView.as_view(), name="dashboard"),
    path('sign-up',sign_up,name='sign_up')

]
