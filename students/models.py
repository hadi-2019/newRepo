from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import AbstractUser


class Student(models.Model):
    STATUS = [
        ('single', 'single'),
        ('married', 'married'),
    ]
    GENDER = [
        ('male', 'male'),
        ('female', 'female'),
    ]
    # personal Information
    kankor_id = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    grand_father_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    main_language = models.CharField(max_length=200, default="دری")
    # phone_number = models.CharField(max_length=100, null=True, blank=True)
    nationality = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS, default="single")
    gender = models.CharField(max_length=10, choices=GENDER, default="male")
    birth_year = models.DateField()

    # address
    main_address = models.CharField(max_length=500, blank=True, null=True)
    current_address = models.CharField(max_length=500, blank=True, null=True)

    # educational information
    school_name = models.CharField(max_length=200)
    graduation_year_from_school = models.DateField()
    kankor_year = models.DateField()
    kankor_score = models.IntegerField()

    # family information
    relative = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=100, blank=True)
    job = models.CharField(max_length=200, blank=True)
    relative_phone_number = models.CharField(max_length=100, blank=True)
    student_registration_date = models.DateField(
        default=timezone.now, null=True, blank=True)

    # national information
    national_id = models.CharField(
        max_length=200, blank=True, null=True)
    page_number = models.CharField(max_length=100, null=True, blank=True)
    register_number = models.CharField(max_length=100, blank=True)
    volume = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(
        upload_to="students/images", default="student.jpg")
    objects = models.Manager()

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse(kwargs={"pk": self.pk})
