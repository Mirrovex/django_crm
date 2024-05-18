from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import SignupForm, AddRecordForm
from .models import Record


def home(request):
    records = Record.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.error(request, "Error, Please try again")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered")
            return redirect('home')
        return render(request, 'register.html', {'form': form})
    else:
        form = SignupForm()
        return render(request, 'register.html', {'form': form})


def customer_record(request, id):
    if request.user.is_authenticated:
        record = Record.objects.get(id=id)
        return render(request, 'record.html', {'record': record})
    else:
        messages.error(request, "You must be logged in to view this page")
        return redirect('home')


def delete_record(request, id):
    if request.user.is_authenticated:
        record = Record.objects.get(id=id)
        record.delete()
        messages.success(request, "Record deleted successfully")
        return redirect('home')
    else:
        messages.error(request, "You must be logged in to view this page")
        return redirect('home')


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                record = form.save()
                messages.success(request, "Record added")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.error(request, "You must be logged in to view this page")
        return redirect('home')
    
def update_record(request, id):
    if request.user.is_authenticated:
        record = Record.objects.get(id=id)
        form = AddRecordForm(request.POST or None, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.error(request, "You must be logged in to view this page")
        return redirect('home')
