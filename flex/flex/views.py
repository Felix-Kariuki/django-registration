from django.shortcuts import render
from flex.models import User
from django.contrib import messages

def IndexPage(request):
    return render(request,'Index.html')

def UserReg(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        Email = request.POST['Email']
        Phone = request.POST['Phone']
        Password  = request.POST['Password']
        User(Name=Name,Email=Email,Phone=Phone,Password=Password).save()
        messages.success(request, 'The new User'+request.POST['Name']+ " Is added succesfully")
        return render(request, 'Registration.html')
    else:
        return render(request, 'Registration.html')