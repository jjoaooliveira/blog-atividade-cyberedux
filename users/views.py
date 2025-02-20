from django.shortcuts import render
from .forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm
from .forms import LoginForm, RegisterForm

def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'users/login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
    
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hi {username.title()}, welcome back!')
                return redirect('/')
        
        messages.error(request, f'Invalid username or password')
        return render(request,'users/login.html',{'form': form})
    
def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/registrar.html', {'form': form}) 
       
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('/')
        else:
            print(form.errors)
            return render(request, 'users/registrar.html', {'form': form})
        
def sign_out(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('login')  

