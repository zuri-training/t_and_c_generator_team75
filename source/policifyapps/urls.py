from django.urls import path
from .views import HomePageView, FeedbackPageView, DashboardPageView
from django.contrib.auth import views
from .views import sign_up , create_policiy_post , create_terms_post , all_post , preview_post , edit_post ,GeneratePdf ,doc_view , policies,delete_post,text_view

from .views import HomePageView, FeedbackPageView, DashboardPageView, PrivacyDashboardPageView, TermsDashboardPageView, ProductPageView, ContactPageView, PPPreviewPageView, TCPreviewPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("home", HomePageView.as_view(), name="home"),
    path("feedback/", FeedbackPageView.as_view(), name="feedback"),
    #path("dashboard/", DashboardPageView.as_view(), name="dashboard"),
    path("product/", ProductPageView.as_view(), name="product"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    #path("privacypolicydashboard/", PrivacyDashboardPageView.as_view(), name="privacypolicydashboard"),
    #path("termsdashboard/", TermsDashboardPageView.as_view(), name="termsdashboard"),
    #path("policypreview/", PolicyPreviewPageView.as_view(), name="policypreview"),
    # path("termspreview/", TermsPreviewPageView.as_view(), name="policypreview"),
    path("tcpreview/", TCPreviewPageView.as_view(), name="tcpreview"),
    path("pppreview/", PPPreviewPageView.as_view(), name="pppreview"),
    
    path("privacypolicydashboard/", create_policiy_post, name="privacypolicydashboard"),
    path("termsdashboard/", create_terms_post, name="termsdashboard"),
    path('sign-up',sign_up,name='sign_up'),
    path('dashboard/',all_post,name='dashboard'),
    path('policypreview/<int:post_type>/<int:my_id>',preview_post,name='preview_post'),
    path('dashboard/policypreview/<int:post_type>/<int:my_id>',preview_post,name='preview_post'),
     path('edit-post/<int:post_type>/<int:my_id>',edit_post,name='edit_post'),
     path('dashboard/edit-post/<int:post_type>/<int:my_id>',edit_post,name='edit_post'),
     path('pdf/<int:post_type>/<int:my_id>', GeneratePdf.as_view()),
     path('dashboard/termsdashboard/',create_terms_post, name="termsdashboard"),
     path("dashboard/privacypolicydashboard/", create_policiy_post, name="privacypolicydashboard"),
     path('word-post/<int:post_type>/<int:my_id>',doc_view,name='word_post'),
      path('policies',policies,name='policies'),
        path('dashboard/policies',policies,name='policies'),
     path('delete-post/<int:post_type>/<int:my_id>',delete_post,name='delete_post'),
       path('dashboard/delete-post/<int:post_type>/<int:my_id>',delete_post,name='delete_post'),
path('text-post/<int:post_type>/<int:my_id>',text_view,name='text_post'),

]
handler404 = 'policifyapps.views.my_custom_page_not_found_view'
handler500 = 'policifyapps.views.my_custom_error_view'
handler403 = 'policifyapps.views.my_custom_permission_denied_view'
handler400 = 'policifyapps.views.my_custom_bad_request_view'