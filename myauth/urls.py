from django.urls import path, include
from . import views

app_name = "appSederhana"   


urlpatterns = [    
    path("", views.home, name="homepage"),
    path('app/', include('appdjango.urls')),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
]