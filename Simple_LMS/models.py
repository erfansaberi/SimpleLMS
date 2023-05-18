from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model


class Course(Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Enrollment(Model):
    student = models.ForeignKey(User, related_name="enrolls", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name="enrolls", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.student} -> {self.course}"
    

class Note(Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/notes')
    is_active = models.BooleanField(default=True)
    upload_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.course} - {self.name}'


class Video(Model):
    subject = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/videos')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.course} - {self.subject}'


class Homework(Model):
    name = models.CharField(max_length=150)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/homeworks')
    solution_file = models.FileField(upload_to='solutions', null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    max_score = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.course}'


class Solution(Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    home_work = models.ForeignKey(Homework, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/student_solutions')
    score = models.IntegerField(null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    is_final = models.BooleanField(default=True)

    def __str__(self):
        if self.is_final and self.score:
            return f'* Final ({self.score} / {self.home_work.max_score}) | {self.student.username} - {self.home_work.name} - {self.upload_date.date()}'
        elif self.is_final and not self.score:
            return f'* Final | {self.student.username} - {self.home_work.name} - {self.upload_date.date()}'
        return f'Non-Final | {self.student.username} - {self.home_work.name} - {self.upload_date.date()}'


class Notification(Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
