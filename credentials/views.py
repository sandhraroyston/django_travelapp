from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def login(request):
    if request.method== 'POST':
        username=request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')

    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')  #to return to homepage
def register(request):

    if request.method == 'POST':
        username=request.POST['username']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        password = request.POST['pw']
        cpassword = request.POST['cpw']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')  #redirect to registration page
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('register')
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            password=password, email=email)
            user.save()
            print("user created...")
            return redirect('login') # to redirect to login page
        else:
            messages.info(request,"Password not matching")
            return redirect('register')

    return render(request,"registration.html")




