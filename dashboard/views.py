from django.shortcuts import render
from students.models import Student
from teachers.models import Teacher


def dashboard(request):
    count = Student.objects.all().count()
    teacherAmount = Teacher.objects.all().count()
    return render(request, "dashboard/index.html", {"count": count, "teacher": teacherAmount})
