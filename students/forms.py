from django import forms
from .models import Student
from django.forms import widgets


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'kankor_id': forms.TextInput(attrs={"class": "form-control", "placeholder": "آی دی "}),
            'first_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "نام کامل"}),
            'father_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "نام پدر"}),
            'grand_father_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "ولدیت"}),
            'last_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "تخلص"}),
            'main_language': forms.TextInput(attrs={"class": "form-control", "placeholder": "زبان اصلی"}),
            'nationality': forms.TextInput(attrs={"class": "form-control", "placeholder": "ملیت"}),
            'status': forms.Select(attrs={"class": "form-control"}),
            'gender': forms.Select(attrs={"class": "form-control"}),
            'nationality': forms.TextInput(attrs={"class": "form-control", "placeholder": "ملیت"}),
            'birth_year': forms.TextInput(attrs={"type": "date", "class": "form-control"}),
            'school_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "مکتب"}),
            'graduation_year_from_school': forms.TextInput(attrs={"type": "date", "class": "form-control"}),
            'kankor_year': forms.TextInput(attrs={"type": "date", "class": "form-control"}),
            'kankor_score': forms.TextInput(attrs={"class": "form-control", "placeholder": "نمره کانکور"}),
            'relative': forms.TextInput(attrs={"class": "form-control", "placeholder": "اقارب"}),
            'name': forms.TextInput(attrs={"class": "form-control", "placeholder": "نام اقارب"}),
            'job': forms.TextInput(attrs={"class": "form-control", "placeholder": "وظیفه"}),
            'relative_phone_number': forms.TextInput(attrs={"class": "form-control", "placeholder": "شماره تماس"}),
            'national_id': forms.TextInput(attrs={"class": "form-control", "placeholder": "نمبر تذکره"}),
            'register_number': forms.TextInput(attrs={"class": "form-control", "placeholder": "شماره ثبت"}),
            'page_number': forms.TextInput(attrs={"class": "form-control", "placeholder": "صفحه"}),
            'volume': forms.TextInput(attrs={"class": "form-control", "placeholder": "جلد"}),

            'main_address': forms.Textarea(attrs={"rows": 3, "placeholder": "ولایت، ولسوالی، ناحیه/قریه...", "class": "form-control"}),
            'current_address': forms.Textarea(attrs={"rows": 3, "placeholder": "ولایت، ولسوالی، ناحیه/قریه...", "class": "form-control"}),
        }
