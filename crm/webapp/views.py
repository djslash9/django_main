from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm

def home(request):
    # check the logged in user
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in')
            
            # redirect to the original page
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out')
    return redirect('home')

def register_view(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You are successfully registered and welcome to the site!')
            return redirect('home')
    else:
        form = RegistrationForm()
    
    # Ensure that the function always returns an HttpResponse object
    return render(request, 'register.html', {'form': form})