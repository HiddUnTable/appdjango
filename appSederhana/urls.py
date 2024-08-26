from django.urls import path
from . import views 
from myauth import views as auth_views

urlpatterns = [ 

path('', views.home, name='home'),
path('register/', auth_views.register_request, name='register_page'),
path('login/', auth_views.login_request, name='login_page'),


path("employees/list/", views.employee_list, name="employee_list"),
path("employees/add/", views.employee_add, name="employee_add"),
path("employees/edit/<str:employee_nip>", views.employee_edit, name="employee_edit"),
path("employees/view/<str:employee_nip>", views.employee_view, name="employee_view"),
path("employees/delete/<str:employee_nip>", views.employee_delete, name="employee_delete"),

]