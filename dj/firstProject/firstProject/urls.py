"""
URL configuration for firstProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from post import views
#To import templateview and redirectview
from django.views.generic.base import TemplateView,RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.home,name="homepage"),
    path("contact-us/",views.contact,name="contact"),
    path("employee/",RedirectView.as_view(url="/admin"),name="employee"),
    path("subject/",views.subjects,name="subject"),
    path("take-data/",views.inputData,name="input"),
    path("submit/",views.submit,name="submit"),
    path("template/",TemplateView.as_view(template_name="template.html",extra_context={"name":"Devaki"}),name='template'),
    path("student/",views.StudentView.as_view(),name="student"),
    
]
