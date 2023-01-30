from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

# Homepage
class HomePageView(TemplateView):
    template_name = 'index.html'

# Login
class LoginPageView(TemplateView):
    template_name = 'login.html'
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.filter(email=email)
        if not user:
            messages.warning(request, 'Username and passowrd does not match')
            print('User does not exist')
            return render(request, self.template_name)
        
        username = user[0].username
        if (authenticate(request, username=username, password=password)):
            login(request, authenticate(request, username=username, password=password))
            messages.success(request, 'Login successful')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Username and passowrd does not match')
            return render(request, self.template_name)

# Logout
def logout_view(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'You are not logged in')
        return redirect('login')
    logout(request)
    messages.success(request, 'Logout successful')
    return redirect('/')

# Register
class RegisterPageView(TemplateView):
    template_name = 'register.html'
    
    def post(self, request):
        username = request.POST.get('studentid')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        
        if (password != confirm_password):
            messages.warning(request, 'Password and confirm password does not match')
            return render(request, self.template_name)
        
        user = User.objects.filter(username=username)
        if user:
            messages.warning(request, 'Student Id already exists')
            return render(request, self.template_name)
        
        user = User.objects.filter(email=email)
        if user:
            messages.warning(request, 'Email already exists')
            return render(request, self.template_name)
        
        user = User.objects.create_user(username=username, email=email, password=password, first_name=firstname, last_name=lastname)
        user.save()
        messages.success(request, 'Registration successful')
        return redirect('login')
    
# Dashboard
class DashboardPageView(LoginRequiredMixin ,TemplateView):
    login_url = 'login'
    template_name = 'dashboard.html'