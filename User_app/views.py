from django.shortcuts import render, redirect
from .forms import CustomRegisterForm
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method =="POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("New User Account Created, Login To Get Started!"))
            return redirect('register')
        else:
            messages.error(request, "There was an error with your registration. Please try again.")
            print(register_form.errors)  # Log errors in the terminal for debugging

    else:
        register_form = CustomRegisterForm()
    return render(request, 'register.html', {'register_form': register_form})