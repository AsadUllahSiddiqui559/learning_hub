from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from core.models import Student, Class
from rest_framework import serializers
from core.models import User

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # Add custom user fields to the response
        data['user'] = {
            'id': self.user.id,
            'username': self.user.username,
            'email': self.user.email,
            'role': self.user.role,
        }
        return data
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Student
        fields = ['id', 'user']

class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = User
        fields = ['id', 'user']

class ClassSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    students = StudentSerializer(many=True)

    class Meta:
        model = Class
        fields = ['id', 'name', 'subject', 'time', 'zoom_link', 'password', 'teacher', 'students']
        depth = 1