from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import Student
from .forms import StudentRegistrationForm


def student_list(request):
    context = {
        "students": Student.objects.all()
    }
    return render(request, "students/student_list.html", context)


def createNewStudent(request):
    if request.method == 'GET':
        form = StudentRegistrationForm()
        return render(request, 'students/student_form.html', {"form": form})
    else:
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            messages.error(
                request, 'عملیات ناموفقانه بود لطفا دوباره کوشش نمایید ')
            return HttpResponseRedirect(reverse('student-list'))
    messages.success(request, " محصیل جدید موفقانه افزوده شد!")
    return HttpResponseRedirect(reverse('student-create'))


def update_student(request, pk=0):
    if request.method == "GET":
        if pk == 0:
            form = StudentRegistrationForm()
        else:
            student = Student.objects.get(pk=pk)
            form = StudentRegistrationForm(instance=student)
            return render(request, "students/student_detail.html", {"form": form})
    else:
        if pk == 0:
            form = StudentRegistrationForm(request.POST, request.FIELS)
        else:
            student = Student.objects.get(pk=pk)
            form = StudentRegistrationForm(
                request.POST, request.FILES, instance=student)
            if form.is_valid():
                form.save()
            messages.success(request, "تغییرات موفقانه بود")
            return HttpResponseRedirect(reverse(f'student-detail/{pk}'))
