from core.models import User, Teacher, Student, Class
from datetime import time
import random

# Clear existing data
User.objects.all().delete()
Teacher.objects.all().delete()
Student.objects.all().delete()
Class.objects.all().delete()

# Utility to create random time
def random_time():
    return time(random.randint(8, 18), random.choice([0, 30]))

# Seed Users
teachers = []
students = []

for i in range(1, 6):  # 5 Teachers
    user = User.objects.create_user(
        username=f"teacher{i}",
        password="password",
        email=f"teacher{i}@example.com",
        role="teacher"
    )
    teachers.append(user)

for i in range(1, 21):  # 20 Students
    user = User.objects.create_user(
        username=f"student{i}",
        password="password",
        email=f"student{i}@example.com",
        role="student"
    )
    students.append(user)

# Seed Teachers
teacher_profiles = [Teacher.objects.create(user=teacher) for teacher in teachers]

# Seed Students
student_profiles = [Student.objects.create(user=student) for student in students]

# Assign students to teachers randomly
for teacher_profile in teacher_profiles:
    assigned_students = random.sample(student_profiles, k=random.randint(3, 10))  # Each teacher gets 3 to 10 students
    teacher_profile.students.add(*assigned_students)

# Seed Classes
class_names = ["Math", "Physics", "Chemistry", "Biology", "History", "English", "Geography", "Computer Science"]
subjects = [f"{subject} 101" for subject in class_names]

for i in range(1, 11):  # 10 Classes
    teacher = random.choice(teacher_profiles)
    new_class = Class.objects.create(
        name=random.choice(class_names) + f" {i}",
        subject=random.choice(subjects),
        time=random_time(),
        teacher=teacher,
        zoom_link=f"https://zoom.us/j/{random.randint(100000000, 999999999)}",
        password=f"class{i}"
    )
    # Assign random students to each class
    assigned_students = random.sample(student_profiles, k=random.randint(5, 15))  # Each class gets 5 to 15 students
    new_class.students.add(*assigned_students)

print("Extended seed data successfully created!")
