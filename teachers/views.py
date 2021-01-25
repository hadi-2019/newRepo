from django.shortcuts import render
from .models import Teacher
from .forms import TeacherCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


def teacher_list(request):
    context = {
        "teachers": Teacher.objects.all()
    }
    return render(request, "teachers/teacher_list.html", context)


def teacher_create(request):
    if request.method == "GET":
        form = TeacherCreationForm()
        return render(request, 'teachers/teacher_form.html',  {"form": form})
    else:
        form = TeacherCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            messages.error(
                request, 'عملیات ناموفقانه بود لطفا دوباره کوشش نمایید')
            return HttpResponseRedirect(reverse('teacher-create'))
    messages.success(request, "عملیات موفقانه انجام شد!")
    return HttpResponseRedirect(reverse('teacher-create'))


def teacher_detail(request, pk):
    if request.method == "GET":
        if pk == 0:
            form = TeacherCreationForm()
        else:
            teacher = Teacher.objects.get(pk=pk)
            form = TeacherCreationForm(instance=teacher)
            return render(request, "teachers/teacher_detail.html", {"form": form, "teacher": Teacher.objects.get(pk=pk)})
    else:
        if pk == 0:
            form = TeacherCreationForm(request.POST, request.FIELS)
        else:
            teacher = Teacher.objects.get(pk=pk)
            form = TeacherCreationForm(
                request.POST, request.FILES, instance=teacher)
            if form.is_valid():
                form.save()
            messages.success(request, "تغییرات موفقانه بود")
            return HttpResponseRedirect(reverse('teacher-detail'))
