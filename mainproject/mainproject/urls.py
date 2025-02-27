"""mainproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from app7 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('hrm/', views.hrm),
    path('employee/', views.employee),
    path('base/', views.base),
    path('accounts/', include('django.contrib.auth.urls')),
    path('form/', views.insert_view),
    path('sample/', views.sample_view),
    path('delete/<int:id>', views.delete_view),
    path('update/<int:id>', views.update_view),
    path('newsdata/', views.newsdata),
    path('newsform/', views.newsform),
    path('holiday/', views.holiday),
    path('calender/', views.calender),
    path('calenderholiday/', views.calenderholiday),
    path('signup/', views.signup_view),






]
