from django.urls import path
from .views import HomePageView, FeedbackPageView, DashboardPageView
from django.contrib.auth import views
from .views import sign_up , create_policiy_post , create_terms_post , all_post , preview_post , edit_post ,GeneratePdf

from .views import HomePageView, FeedbackPageView, DashboardPageView, PrivacyDashboardPageView, TermsDashboardPageView, PolicyPreviewPage, ProductPageView, ContactPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("home", HomePageView.as_view(), name="home"),
    path("feedback/", FeedbackPageView.as_view(), name="feedback"),
    #path("dashboard/", DashboardPageView.as_view(), name="dashboard"),
    path("product/", ProductPageView.as_view(), name="product"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    #path("privacypolicydashboard/", PrivacyDashboardPageView.as_view(), name="privacypolicydashboard"),
    #path("termsdashboard/", TermsDashboardPageView.as_view(), name="termsdashboard"),
    # path("policypreview/", PolicyPreviewPage.as_view(), name="policypreview"),
    path("privacypolicydashboard/", create_policiy_post, name="privacypolicydashboard"),
    path("termsdashboard/", create_terms_post, name="termsdashboard"),
    path('sign-up',sign_up,name='sign_up'),
    path('dashboard/',all_post,name='dashboard'),
    path('policypreview/<int:post_type>/<int:my_id>',preview_post,name='preview_post'),
     path('edit-post/<int:my_id>',edit_post,name='edit_post'),
     path('pdf/<int:post_type>/<int:my_id>', GeneratePdf.as_view()),


]
