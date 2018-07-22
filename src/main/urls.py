"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='MoD-i API', description='dalenge abhi', url='http://ec2-13-232-100-99.ap-south-1.compute.amazonaws.com:8000/')

urlpatterns = [
    path('', 
        include_docs_urls(title='MoD-i API', 
        description='', 
        schema_url='http://ec2-13-232-100-99.ap-south-1.compute.amazonaws.com:8000/')),
    path('schema/', schema_view),
    path('admin/', admin.site.urls),
    path('dep1/', include('dep1.urls', namespace='dep1')),
]
