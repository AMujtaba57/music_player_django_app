from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import RegistrationUser
from .forms import RegisterForm

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

def SignupPage(request):
    if request.method=='POST':
        first_name=request.POST.get('fname')
        last_name=request.POST.get('lname')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            my_user=RegistrationUser.objects.create(first_name=first_name, username=email,
                                                    last_name=last_name, email=email, 
                                                    password=pass1, is_superuser=False, is_staff=False,
                                                    is_active=False)
            if my_user:
                my_user.save()
                return redirect('home')
            return redirect('SignupPage')
    return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        user = RegistrationUser.objects.filter(email=email, password=pass1).exists()
        if user is not None:
            return render(request, "home.html")
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render(request,'login.html')


def logoutPage(request):
    """
    If the user is logged in, log them out and redirect them to the login page
    
    :param request: The request is an HttpRequest object
    :return: the redirect function.
    """
    if request:
        logout(request)
    return redirect('login')