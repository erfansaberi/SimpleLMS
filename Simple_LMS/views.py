from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
# Create your views here.

# Homepage
class HomePageView(TemplateView):
    template_name = 'index.html'

# Signin
class SigninPageView(TemplateView):
    template_name = 'signin.html'
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        if (authenticate(request, username=username, password=password)):
            login(request, authenticate(request, username=username, password=password))
            return render(request, 'index.html')
        return render(request, self.template_name)