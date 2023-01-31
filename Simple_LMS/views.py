import collections
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView

from .models import *


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

        user = User.objects.create_user(username=username, email=email, password=password, first_name=firstname,
                                        last_name=lastname)
        user.save()
        messages.success(request, 'Registration successful')
        return redirect('login')


# Dashboard
class DashboardPageView(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    template_name = 'dashboard.html'

    def get(self, request):
        notifications = Notification.objects.order_by('-id')[0:5]
        active_homework = Homework.objects.filter(is_active=True).first()
        context = {'notifications': notifications, 'active_homework': active_homework}
        return render(request, self.template_name, context)


class SolutionUpload(LoginRequiredMixin, View): # TODO: BUG - Solution upload not working
    def post(self, request: HttpRequest):
        user = request.user
        homework_id = request.POST.get('homework_id')
        user_solution = request.POST.get('solution')
        homework = Homework.objects.filter(id=homework_id).first()
        solution = Solution(student=user, home_work=homework, file=user_solution)
        solution.save()
        messages.success(request, 'Solution uploaded successfully')
        return redirect(self.request.META.get('HTTP_REFERER'))


class NotificationsPageView(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    template_name = 'notifications.html'

    def get(self, request):
        notifications = Notification.objects.order_by('-id')
        return render(request, self.template_name, {'notifications': notifications})


class VideosPageView(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    template_name = 'videos.html'

    def get(self, request):
        videos = Video.objects.order_by('-id')
        return render(request, self.template_name, {'videos': videos})


class HomeworksPageView(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    template_name = 'homeworks.html'

    def get(self, request):
        homeworks = Homework.objects.order_by('-id')
        student_solutions = Solution.objects.filter(student=request.user).order_by('-id')
        homework_and_solution = collections.namedtuple('HomeworkAndSolution', ['homework', 'studentsolution'])
        homeworks_and_solutions = []
        for homework in homeworks:
            for solution in student_solutions:
                if solution.home_work == homework:
                    homeworks_and_solutions.append(homework_and_solution(homework, solution))
                    break
            else:
                homeworks_and_solutions.append(homework_and_solution(homework, None))
        
        return render(request, self.template_name, {"homeworks_and_solutions": homeworks_and_solutions})