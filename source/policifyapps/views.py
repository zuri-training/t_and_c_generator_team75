from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from . forms import RegistrationForm , PoliciesForm , TermsForm
from django.contrib.auth.decorators import login_required
from .models import PolicyPost, TermPost

# importing the necessary libraries
from django.http import HttpResponse
from django.views.generic import View
from .process import html_to_pdf 
from django.template.loader import render_to_string

from htmldocx import HtmlToDocx
import os
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
    
class PolicyPreviewPageView(TemplateView):
    template_name = "dashboard/policypreview.html"
    
class TermsPreviewPageView(TemplateView):
    template_name = "dashboard/termspreview.html"

class ProductPageView(TemplateView):
    template_name = "product.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"
   
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

  
def preview_post(request, post_type,my_id):
     if post_type == 1:
         posts = PolicyPost.objects.get(id= my_id)
         return render(request,"dashboard/policypreview.html",{"posts":posts})
     if post_type == 2:
          posts = TermPost.objects.get(id= my_id)
          return render(request,"dashboard/termspreview.html",{"posts":posts})
     return render(request,"dashboard/policypreview.html",{"posts":posts})

def doc_view(request,post_type,my_id):
        print(request) 
        if post_type == 1:
            data = PolicyPost.objects.filter(id=my_id).first()
            open('templates/temp.html', "w").write(render_to_string('pdf.html', {'posts': data}))
        if post_type == 2:
            data = TermPost.objects.filter(id=my_id).first()
            open('templates/temp.html', "w").write(render_to_string('pdf2.html', {'posts': data}))
        new_parser = HtmlToDocx()
        new_parser.parse_html_file('templates/temp.html',"html-word")
        file_path = os.path.abspath("html-word.docx")
        print('SLA FILE' ,file_path)
        if os.path.exists(file_path):
          print("it exist!")
          with open(file_path,'rb') as worddoc: # read as binary
               content = worddoc.read() # read the file
               print("reading the file...")
               response = HttpResponse(
                    content,
                    content_type = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
               )
               response['Content-Disposition'] = 'attachment; filename=download_filename.docx'
               response['Content-Length'] = len(content) #calculate the length of content
               return response
        else:
          print("path doesnt' exist")
          return HttpResponse("Failed to Download SLA")




def edit_post(request,post_type ,my_id):
     if post_type == 1:
        obj = get_object_or_404(PolicyPost,id=my_id)
        form = PoliciesForm(request.POST or None, instance=obj)
     if post_type == 2:
        obj = get_object_or_404(TermPost,id=my_id)
        form = TermsForm(request.POST or None, instance=obj)
     if form.is_valid():
          form.save()
          return redirect("/dashboard")
     return render(request, "dashboard/edit_post.html",{'form': form})

#Creating a class based view
class GeneratePdf(View):
     def get(self, request,post_type, my_id):
        if post_type == 1:
            print(request)
            data = PolicyPost.objects.filter(id=my_id).first()
            open('templates/temp.html', "w").write(render_to_string('pdf.html', {'posts': data}))
            # Converting the HTML template into a PDF file
            pdf = html_to_pdf('temp.html')
            # rendering the template
            # return FileResponse(pdf,as_attachment=True, filename='venue.pdf')
            return HttpResponse(pdf, content_type='application/pdf')

        if post_type == 2:
            data = TermPost.objects.filter(id=my_id).first()
            open('templates/temp.html', "w").write(render_to_string('pdf2.html', {'posts': data}))
            # Converting the HTML template into a PDF file
            pdf = html_to_pdf('temp.html')
            # rendering the template
            # return FileResponse(pdf,as_attachment=True, filename='venue.pdf')
            return HttpResponse(pdf, content_type='application/pdf')
        
        