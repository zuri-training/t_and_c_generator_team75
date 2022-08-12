from django.urls import path
from .views import HomePageView, FeedbackPageView, DashboardPageView
from django.contrib.auth import views
from .views import sign_up , create_policiy_post , create_terms_post , all_post

from .views import HomePageView, FeedbackPageView, DashboardPageView, PrivacyDashboardPageView, TermsDashboardPageView, PolicyPreviewPage

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("home", HomePageView.as_view(), name="home"),
    path("feedback/", FeedbackPageView.as_view(), name="feedback"),
    # path("dashboard/", DashboardPageView.as_view(), name="dashboard"),
    #path("privacypolicydashboard/", PrivacyDashboardPageView.as_view(), name="privacypolicydashboard"),
    #path("termsdashboard/", TermsDashboardPageView.as_view(), name="termsdashboard"),
    path("policypreview/", PolicyPreviewPage.as_view(), name="policypreview"),
    path("privacypolicydashboard/", create_policiy_post, name="privacypolicydashboard"),
    path("termsdashboard/", create_terms_post, name="termsdashboard"),
    path('sign-up',sign_up,name='sign_up'),
    path('dashboard/',all_post,name='dashboard')


]
