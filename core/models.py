from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings 


class User(AbstractUser):
    ROLE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')


class Teacher(models.Model):
    # Use settings.AUTH_USER_MODEL to reference the custom User model
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="teacher_profile")
    students = models.ManyToManyField("Student", related_name="teachers", blank=True)

    def __str__(self):
        return self.user.username


class Student(models.Model):
    # Use settings.AUTH_USER_MODEL to reference the custom User model
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="student_profile")

    def __str__(self):
        return self.user.username


class Class(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    time = models.TimeField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="classes")
    zoom_link = models.URLField()
    password = models.CharField(max_length=255)
    students = models.ManyToManyField(Student, related_name="classes", blank=True)

    def __str__(self):
        return f"{self.name} - {self.subject} (Teacher: {self.teacher.user.username})"
