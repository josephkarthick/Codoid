from django.shortcuts import render,redirect
from login.models import codoid_login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages

def home(request):
    return render (request, 'index.html')

def signin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password )
        
        if user is not None:
            login (request,user)
            return render(request, 'index.html')
        else:
            messages.success(request, ("Check User Name And Password"))
            return redirect('signin')
    return render(request, 'sign_in.html')
    
def signup(request):
    if request.method == 'POST':
        username = request.POST ['username']
        email = request.POST ['email']
        password = request.POST ['password']
        qry = User.objects.create(username = username, email = email, password = password)
        qry.save()
    return render(request, 'sign_up.html')
    
