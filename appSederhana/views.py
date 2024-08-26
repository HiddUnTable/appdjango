import bcrypt
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import EmployeeAdd, new_user
from .forms import EmployeeForm, registrationForm, RegistForm, LoginForm
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html')

# def registration(request):
#     if request.method == 'POST':
#         post = request.POST
#         email = post.get('email')
#         password = post.get('password')
#         password2 = post.get('password2')
#         full_name = post.get('full_name')
#         birth_date = post.get('birth_date')

#         check = new_user.objects.filter(email=post.get('email'))
#         if post.get('password') != post.get('password2'):
#             messages.error(request, 'Confirm password does not match')
#         elif check.exists():
#             messages.error(request, 'Email does exist')
#         else:
#             hashed_password = hash_password(password)
#             form = RegistForm({
#                 'email' : email,
#                 'full_name' : full_name,
#                 'birth_date' : birth_date,
#                 'password' : hashed_password,
#             })  
            
#             if form.is_valid():
#                 user = form.save(commit=False)
#                 # user.password = hashed_password.decode('utf-8') # buat apa decode???
#                 user.save()
#                 return redirect('login')
#             else:
#                 messages.error(request, form.errors)

#     return render(request, 'registration.html')

# def hash_password(password):
#     salt = bcrypt.gensalt()
#     hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
#     return hashed_password.decode('utf-8')

# def login(request):
    if request.method =='POST':
        print("SATU")
        form = LoginForm (request, data=request.POST)
        print(form)
        print("DUA")
        if form.is_valid():
            print("TIGA")
            form.save()
            print("EMPAT")
            return redirect('employee_list')
        else:
            print("EMPAT")
            messages.error(request, form.errors)
    else: 
       form = LoginForm()

    return render(request, 'login.html', {'forms': form})

def employee_list(request):
    employee_data = EmployeeAdd.objects.all().order_by('-id')
    return render(request, 'employee_list.html', {'employees': employee_data})


def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)   
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee added successfully!')
            return redirect('employee_list')
        else:
             messages.error(request, 'Error: Employee with this NIP already exists.')
    else:
        form = EmployeeForm()

    return render(request, 'employee_add.html', {'form': form}) 

def employee_view(request, employee_nip):
    employee = EmployeeAdd.objects.get(nip = employee_nip)
    if employee:
        return render(request, 'employee_view.html', {'employees':employee})
    else:
        return redirect('employee_list')

def employee_edit(request, employee_nip):
    nip = int(employee_nip)
    employee = EmployeeAdd.objects.get(nip = employee_nip)

    if request.method =='POST':
        form = EmployeeForm(request.POST, instance= employee)
        if form.is_valid():
            form.save()
            return redirect('employee_view', employee_nip=employee.nip)
        else:
            print("ERROR", form.errors)
    else:
        form= EmployeeForm(instance=employee)

    return render(request, 'employee_edit.html', {'form':form, 'employee': employee})

def employee_delete(request, employee_nip):
    nip = int(employee_nip)
    employee = EmployeeAdd.objects.get(nip = employee_nip)

    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')

    return render(request,'employee_delete.html', {'employees': employee})
