from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.db.models import Model



class Course(Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField()

    def __str__(self):
        return self.name


class Notes(Model):
    number = models.IntegerField(unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/notes')
    is_active = models.BooleanField()

    def __str__(self):
        return f'{self.course} - {self.number}'


class Videos(Model):
    subject = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/videos')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_active = models.BooleanField()

    def __str__(self):
        return f'{self.course} - {self.subject}'


class Homeworks(Model):
    name = models.CharField(max_length=150)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    file = models.FileField(upload_to='upload/homeworks')
    solution_file = models.FileField(upload_to='upload/solutions')
    is_active = models.BooleanField(unique=True)

    def __str__(self):
        return f'{self.name} - {self.course}'


class Solutions(Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    home_work = models.ForeignKey(Homeworks, on_delete=models.CASCADE)
    file = models.FileField('uploads/studentsolutions')
    upload_date = models.DateTimeField(auto_now_add=True)


class Notifications(Model):
    text = models.TextField()
    image = models.ImageField(upload_to='upload/notificationimgs')
    timestamp = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(unique=True)
