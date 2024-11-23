from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    students = models.ManyToManyField("Student", related_name="teachers", blank=True)

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    time = models.TimeField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="classes")
    zoom_link = models.URLField()
    password = models.CharField(max_length=255)
    students = models.ManyToManyField("Student", related_name="classes", blank=True)

    def __str__(self):
        return f"{self.name} - {self.subject} (Teacher: {self.teacher.name})"


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name