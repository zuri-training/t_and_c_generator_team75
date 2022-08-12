from django.contrib import admin
from .models import PolicyPost, TermPost

# Register your models here.
admin.site.register(PolicyPost)
admin.site.register(TermPost)