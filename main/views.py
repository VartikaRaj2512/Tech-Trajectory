from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from main.forms import RegistrationForm,LevelSelectionForm
from .forms import LevelSelectionForm
from .models import LevelSelection
# Home Page
def home(request):
    return render(request, 'main/index.html')

# About Page
def about(request):
    return render(request, 'main/about.html')

# Contact Page
def contact(request):
    return render(request, 'main/contact.html')

# Services Page
def services(request):
    return render(request, 'main/services.html')

# Register Page
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Save the user to the database
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Set the password securely
            user.save()
            messages.success(request, "Account created successfully. You can now log in.")
            login(request, user)  # Automatically log the user in after successful registration
            return redirect('home')
        else:
            messages.error(request, "There was an error with your registration. Please try again.")
    else:
        form = RegistrationForm()

    return render(request, 'main/register.html', {'form': form})

# Login Page
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

# Logout
def user_logout(request):
    logout(request)
    return redirect('home')



# data form 

def level_selection_view(request):
    if request.method == 'POST':
        form = LevelSelectionForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('level_selection_success')  # Redirect to a success page (optional)
    else:
        form = LevelSelectionForm()

    return render(request, 'main/level_selection_form.html', {'form': form})

# views.py
def level_selection_success(request):
    data = LevelSelection.objects.last()
    return render(request, 'main/level_selection_result.html',{'data':data})
