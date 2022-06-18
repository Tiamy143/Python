from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method == 'POST':
        uname=request.POST['username']
        password = request.POST['pass']
        user = auth.authenticate(username=uname, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')
    return render(request, "login.html")
def register(request):
    if request.method == 'POST':
        uname=request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['pass']
        cpass = request.POST['conpass']
        if password == cpass:
            if User.objects.filter(username=uname).exists():
                messages.info(request, "Username exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email ID exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=password)

                user.save()
                return redirect('login')

        else:
            messages.info(request, "Password not matched")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")