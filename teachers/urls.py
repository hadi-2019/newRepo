from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import teacher_list, teacher_create, teacher_detail


urlpatterns = [
    path('teacher_list/', teacher_list, name="teacher-list"),
    path('teacher/add/', teacher_create, name="teacher-create"),
    path('teacher/<int:pk>/', teacher_detail, name="teacher-detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
