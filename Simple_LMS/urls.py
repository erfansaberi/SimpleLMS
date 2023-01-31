from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('login/', views.LoginPageView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.RegisterPageView.as_view(), name='register'),
    path('dashboard/', views.DashboardPageView.as_view(), name='dashboard'),
    path('dashboard/notifications', views.NotificationsPageView.as_view(), name='notifications'),
    path('dashboard/videos', views.VideosPageView.as_view(), name='videos'),
    path('dashboard/homeworks', views.HomeworksPageView.as_view(), name='homeworks'),
    path('dashboard/solution-upload/', views.SolutionUpload.as_view(), name='solution'),
]
