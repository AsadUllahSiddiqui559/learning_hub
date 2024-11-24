from django.urls import path
from core.views import StudentListView, StudentDetailView, StudentClassesView
from core.views import TeacherListView, TeacherDetailView, TeacherClassesView
from .views import CustomTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [

  # authentication related apis
  path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

  # students related apis
  path('api/students/', StudentListView.as_view(), name='student_list'),
  path('api/students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
  path('api/students/classes/', StudentClassesView.as_view(), name='student_classes'),

  # teachers related apis
  path('api/teachers/', TeacherListView.as_view(), name='teacher_list'),
  path('api/teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),
  path('api/teachers/classes/', TeacherClassesView.as_view(), name='teacher_classes'),
]