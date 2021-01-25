from django.urls import path
from .views import student_list, createNewStudent, update_student


urlpatterns = [
    path('students', student_list, name="student-list"),
    path('student/add/', createNewStudent, name="student-create"),
    path('student/detail/<int:pk>/', update_student, name="student-detail"),
]
