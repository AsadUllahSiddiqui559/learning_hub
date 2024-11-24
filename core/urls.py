from django.urls import path
from core.views import StudentListView
from core.views import StudentDetailView
from core.views import StudentClassesView
from .views import CustomTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('api/token/', CustomTokenObtainPairView.as_view()  , name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # students related apis
    path('api/students/', StudentListView.as_view(), name='student_list'),
    path('api/students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('api/students/classes/', StudentClassesView.as_view(), name='student_classes'),
]