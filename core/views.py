from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View


@login_required
def home(request):
    return render(request, 'home.html')

class Signup(View):
    def get (self,request):
        form = UserCreationForm(request.GET)
        return render(request, 'signup.html', {'form': form})
    def post(self,request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.post('username')
                raw_password = form.cleaned_data.post('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                form.save()
                return redirect('home')
        else:
            form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})