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

import re
from django.utils.html import strip_tags
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
    template_name ="index.html"
    
class FeedbackPageView(TemplateView):
    template_name = "feedback.html"

@login_required(login_url="/login") 
class DashboardPageView(TemplateView):
    template_name = "dashboard/dashboard.html"
    
@login_required(login_url="/login")   
class PrivacyDashboardPageView(TemplateView):
    template_name = "dashboard/privpolicydash.html"

@login_required(login_url="/login")
class TermsDashboardPageView(TemplateView):
    template_name = "dashboard/termscondash.html"

# @login_required(login_url="/login")   
# class PolicyPreviewPageView(TemplateView):
#     template_name = "dashboard/policypreview.html"

# @login_required(login_url="/login")   
# class TermsPreviewPageView(TemplateView):
#     template_name = "dashboard/termspreview.html"

class ProductPageView(TemplateView):
    template_name = "product.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"

class TCPreviewPageView(TemplateView):
    template_name = "tcp.html"
    
class PPPreviewPageView(TemplateView):
    template_name = "ppp.html"   

   
@login_required(login_url="/login")
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

@login_required(login_url="/login")
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

@login_required(login_url="/login")
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


def textify(html):
    # Remove html tags and continuous whitespaces 
    text_only = re.sub('[ \t]+', ' ', strip_tags(html))
    # Strip single spaces in the beginning of each line
    return text_only.replace('\n ', '\n').strip()

def text_view(request,post_type,my_id):
        print(request) 
        if post_type == 1:
            data = PolicyPost.objects.filter(id=my_id).first()
            open('templates/temp.html', "w").write(render_to_string('pdf.html', {'posts': data}))
        if post_type == 2:
            data = TermPost.objects.filter(id=my_id).first()
            open('templates/temp.html', "w").write(render_to_string('pdf2.html', {'posts': data}))
        html = render_to_string('temp.html')
        text = textify(html)
        print(text)
        response = HttpResponse(
                    text,
                    content_type = 'text/plain'
               )
        response['Content-Disposition'] = 'attachment; filename=download_filename.txt'
        response['Content-Length'] = len(text) #calculate the length of content
        return response

def policies(request):
    return render(request,"dashboard/policies.html",{})

@login_required(login_url="/login")
def edit_post(request,post_type ,my_id):
     if post_type == 1:
        obj = get_object_or_404(PolicyPost,id=my_id)
        form = PoliciesForm(request.POST or None, instance=obj)
        if form.is_valid():
          form.save()
          return redirect("/dashboard")
        return render(request, "dashboard/edit_policy_post.html",{'form': form})
     if post_type == 2:
        obj = get_object_or_404(TermPost,id=my_id)
        form = TermsForm(request.POST or None, instance=obj)
        if form.is_valid():
          form.save()
          return redirect("/dashboard")
        return render(request, "dashboard/edit_term_post.html",{'form': form})

@login_required(login_url="/login")     
def delete_post(request,post_type,my_id):
      if post_type == 1:
        post = PolicyPost.objects.filter(id=my_id).first()
        if post and post.author == request.user:
             post.delete()
             return redirect("/dashboard")
      if post_type == 2:
         post = PolicyPost.objects.filter(id=my_id).first()
         if post and post.author == request.user:
             post.delete()
             return redirect("/dashboard")

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

def my_custom_page_not_found_view(request,exception):
    return render(request, '404.html',{})

def my_custom_error_view(request,exception=None):
    return render(request, '500.html',{})

def my_custom_permission_denied_view(request,exception=None):
    return render(request, '403.html',{})

def my_custom_bad_request_view(request,exception=None):
    return render(request, '400.html',{})        
        