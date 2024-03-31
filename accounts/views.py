from django.shortcuts import render

# Create your views here.

# def index(request):
#     return render(request, "accounts/index.html")

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.conf import settings

def register(request):
    if not settings.ALLOW_PUBLIC_REGISTRATION and not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:index')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})


def accounts_home(request):
    return render(request, 'accounts/index.html')
