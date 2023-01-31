from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model



class Course(Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField()

    def __str__(self):
        return self.name


class Note(Model):
    number = models.IntegerField(unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    file = models.FileField(upload_to='notes')
    is_active = models.BooleanField()

    def __str__(self):
        return f'{self.course} - {self.number}'


class Video(Model):
    subject = models.CharField(max_length=100)
    file = models.FileField(upload_to='videos')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_active = models.BooleanField()

    def __str__(self):
        return f'{self.course} - {self.subject}'


class Homework(Model):
    name = models.CharField(max_length=150)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    file = models.FileField(upload_to='homeworks')
    solution_file = models.FileField(upload_to='solutions', null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField()

    def __str__(self):
        return f'{self.name} - {self.course}'


class Solution(Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    home_work = models.ForeignKey(Homework, on_delete=models.CASCADE)
    file = models.FileField('studentsolutions')
    upload_date = models.DateTimeField(auto_now_add=True)


class Notification(Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField()
    
    def __str__(self):
        return self.title
