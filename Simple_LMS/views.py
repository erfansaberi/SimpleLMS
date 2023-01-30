from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
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
            return render(request, 'index.html')
        else:
            messages.warning(request, 'Username and passowrd does not match')
            return render(request, self.template_name)