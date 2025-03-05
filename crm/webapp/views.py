from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm, AddClientForm
from .models import Client

def home(request):
    
    # Grab client records
    clients = Client.objects.all()
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
        return render(request, 'home.html', {'clients': clients})

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

def client(request, pk):
    if request.user.is_authenticated:
        # look up the specific client data
        client_record = Client.objects.get(id=pk)
        return render(request, 'client.html', {'client_record': client_record})
    else:
        messages.error(request, 'You need to be logged in to view this page')
        return redirect('home')
    
def client_delete(request, pk):
    if request.user.is_authenticated:
        # look up the specific client data
        delete_record = Client.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, 'Client record has been deleted')
        return redirect('home')
    else:
        messages.error(request, 'You need to be logged in to view this page')
        return redirect('home')

def add_client(request):
    form = AddClientForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method =="POST":
            if form.is_valid:
                add_client = form.save()
                messages.success(request, 'Client has been added')
                return redirect('home')
        return render(request, 'add_client.html', {'form':form})
                
    else:
        messages.error(request, 'You need to be logged in to view this page')
        return redirect('home')
