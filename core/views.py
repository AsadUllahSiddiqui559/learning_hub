from django.shortcuts import render
from rest_framework.generics import ListAPIView
from core.models import Student, Teacher
from core.serializers import StudentSerializer, ClassSerializer, TeacherSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

# students
class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

class StudentDetailView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

class StudentClassesView(ListAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
      if request.user.role != 'student':
        return Response({"error": "You are not a student"}, status=status.HTTP_400_BAD_REQUEST)

      try:
        student = Student.objects.get(user=request.user)
        classes = student.classes.all()
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data)
      except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

# Teachers
class TeacherListView(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]

class TeacherDetailView(RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]

class TeacherClassesView(ListAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
      if request.user.role != 'teacher':
        return Response({"error": "You are not a teacher"}, status=status.HTTP_400_BAD_REQUEST)

      try:
        teacher = Teacher.objects.get(user=request.user)
        classes = teacher.classes.all()
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data)
      except teacher.DoesNotExist:
        return Response({"error": "teacher not found"}, status=status.HTTP_404_NOT_FOUND)


