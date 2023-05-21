from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from .models import *
from django.contrib import messages

# Create your views here.
from django.contrib.auth import authenticate, login, logout

class SignUp(View):
    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'signup.html', {'form':form})
    def post(self, request, *args, **kwargs):
        form_data = SignUpForm(data=request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Account Created.")
            return redirect('login')
        else:
            messages.error(request, "Not a valid entry!")
            return render(request, "signup.html", {'form':form_data})

class LogIn(View):
    def get(self, request, *args, **kwargs):
        form = SignInForm()
        return render(request, 'login.html', {'form':form})
    def post(self, request, *args, **kwargs):
        form_data = SignInForm(data = request.POST)
        if form_data.is_valid():
            uname = form_data.cleaned_data.get("username")
            pswd = form_data.cleaned_data.get("password")
            user = authenticate(request, username= uname, password = pswd)
            if user:
                login(request, user)
                messages.success(request, "Sign in completed")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or Password")
                return render(request, "login.html", {"form":form_data})
        else:
            return render(request, "login.html", {"form":form_data})

    
class LogOut(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')
    
from datetime import datetime
class Home(View):
    def get(self, request, *args, **kwargs):
        user_obj = request.user
        uname = user_obj.username
        form = ToDoForm(instance=user_obj)
        data = ToDoModel.objects.filter(username=uname)        
        return render(request, 'home.html', {'user': user_obj, 'form':form, 'data':data})
    def post(self, request, *args, **kwargs):
        form_data = ToDoForm(data = request.POST)
        form_data.instance.username = self.request.user 
        form_data.instance.createddt = datetime.now()
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Event added")
            return redirect('home')
        else:
            messages.error(request, 'Something error!')
            return render(request, 'home.html', {'form':form_data})

class Update(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        obj = ToDoModel.objects.get(id=id)
        form = ToDoForm(instance=obj)
        return render(request, 'update.html', {'form':form})
    def post(self, request, *args, **kwargs):
        id = kwargs.get('id')
        obj = ToDoModel.objects.get(id=id)
        form_data = ToDoForm(data=request.POST, instance=obj)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Updation successfull")
            return redirect("home")
        else:
            return render(request, "update.html", {"form":form_data})

class Delete(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        obj = ToDoModel.objects.get(id=id)
        obj.delete()
        return redirect('home')