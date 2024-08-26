"""appdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from myauth import views as auth_views
from appSederhana import views 

urlpatterns = [
    # path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('register/', auth_views.register_request, name='register_page'),
    path('login/', auth_views.login_request, name='login_page'),

    path("employees/list/", views.employee_list, name="employee_list"),
    path("employees/add/", views.employee_add, name="employee_add"),
    path("employees/view/<str:employee_nip>", views.employee_view, name="employee_view"),
    path("employees/edit/<str:employee_nip>", views.employee_edit, name="employee_edit"),
    path("employees/delete/<str:employee_nip>", views.employee_delete, name="employee_delete"),
]

