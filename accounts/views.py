from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print("username==============>",username)
        print("password===============>",password)
        user = authenticate(username=username, password=password)
        print("user===========>",user)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Bad credentials")
            return redirect('home')
    return render(request, 'accounts/signin.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username")
            return redirect('signup')

        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('signup')

        if len(username) > 10:
            messages.error(request, "Username should not be more than 10 characters")
            return redirect('signup')

        if password1 != password2:
            messages.error(request, "Password didn't match")
            return redirect('signup')

        if not username.isalnum():
            messages.error(request, "Username should be Alphanumeric")
            return redirect('signup')

        myuser = User.objects.create_user(username, email, password1)
        myuser.save()
        messages.success(request, "Your account has been successfully created.")
        return redirect('signin')
    else:
        return render(request, 'accounts/signup.html')

def signout(request):
    auth.logout(request)
    messages.success(request, "Logged out Successfully")
    return redirect('home')
