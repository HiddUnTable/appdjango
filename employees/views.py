from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Employee
from .forms import EmployeeForm

# Create your views here.

# class CustomLoginView(LoginView):
#     template_name='login.html'
#     redirect_authenticated_user = True

# def employee_add(request):
#     if request.method=='POST':
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('employee_list')
#         else: 
#             form =EmployeeForm()
        
#         return render(request, 'employee_add.html', {'form', form})     

# def employee_list(request):
#     employees = Employee.objects.all()
#     return render(request, 'employee_list.html', {'employees': employees})
