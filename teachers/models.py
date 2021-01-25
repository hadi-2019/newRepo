from django.db import models
from django.utils import timezone


class Teacher(models.Model):
    GENDER = [
        ("male", "male"),
        ("female", "female"),
    ]
    STATUS = [
        ("single", "single"),
        ("married", "married")
    ]
    ARMY = [
        ("Yes", "yes"),
        ("No", "no"),
    ]
    # personal Information
    teacher_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=200)
    birth_year = models.DateField(null=True, blank=True)
    birth_place = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=GENDER, default="male")
    status = models.CharField(max_length=20, choices=STATUS, default="single")
    nationality = models.CharField(max_length=200)
    army_job = models.CharField(max_length=10, choices=ARMY, default="Yes")
    # national Card information
    national_id = models.CharField(max_length=200, null=True, blank=True)
    register_number = models.CharField(max_length=200, null=True, blank=True)
    page_number = models.CharField(max_length=200, null=True, blank=True)
    volume = models.CharField(max_length=200, null=True, blank=True)
    # Education Information
    high_school_name = models.CharField(max_length=200)
    high_school_location = models.CharField(max_length=200)
    high_school_start = models.DateField(null=True, blank=True)
    high_school_end = models.DateField(null=True, blank=True)
    hight_school_field = models.CharField(
        max_length=200, null=True, blank=True)
    high_school_diploma = models.ImageField(upload_to="teacher/school/")
    high_school_percentage = models.CharField(max_length=200)

    bachelor_university_name = models.CharField(max_length=200)
    bachelor_university_location = models.CharField(max_length=200)
    bachelor_start = models.DateField(null=True, blank=True)
    bachelor_end = models.DateField(null=True, blank=True)
    bachelor_field = models.CharField(max_length=200)
    bachelor_diploma = models.ImageField(upload_to="teacher/bachelor/")
    bachelor_percentage = models.CharField(max_length=200)

    master_university_name = models.CharField(
        max_length=200, null=True, blank=True)
    master_university_location = models.CharField(
        max_length=200, null=True, blank=True)
    master_start = models.DateField(null=True, blank=True)
    master_end = models.DateField(null=True, blank=True)
    master_field = models.CharField(max_length=200, null=True, blank=True)
    master_diploma = models.ImageField(
        upload_to="teacher/master/", null=True, blank=True)
    master_percentage = models.CharField(max_length=200, null=True, blank=True)

    phd_university_name = models.CharField(
        max_length=200, null=True, blank=True)
    phd_university_location = models.CharField(
        max_length=200, null=True, blank=True)
    phd_start = models.DateField(null=True, blank=True)
    phd_end = models.DateField(null=True, blank=True)
    phd_field = models.CharField(max_length=200, null=True, blank=True)
    phd_diploma = models.ImageField(
        upload_to="teacher/school/", null=True, blank=True)
    phd_percentage = models.CharField(max_length=200, null=True, blank=True)

    # job experience
    # job_title = models.CharField(max_length=200, null=True)
    job_location = models.CharField(max_length=200, null=True, blank=True)
    job_position = models.CharField(max_length=200, null=True, blank=True)
    job_start_date = models.DateField(null=True, blank=True)
    job_end_date = models.DateField(null=True, blank=True)
    recomandition_letter = models.ImageField(
        upload_to="teacher/jon/", null=True, blank=True)

    # job experience
    # job_title = models.CharField(max_length=200, null=True)
    job_location2 = models.CharField(max_length=200, null=True, blank=True)
    job_position2 = models.CharField(max_length=200, null=True, blank=True)
    job_start_date2 = models.DateField(null=True, blank=True)
    job_end_date2 = models.DateField(null=True, blank=True)
    recomandition_letter2 = models.ImageField(
        upload_to="teacher/job2/", null=True, blank=True)

    # job experience
    # job_title = models.CharField(max_length=200, null=True)
    job_location3 = models.CharField(max_length=200, null=True, blank=True)
    job_position3 = models.CharField(max_length=200, null=True, blank=True)
    job_start_date3 = models.DateField(null=True, blank=True)
    job_end_date3 = models.DateField(null=True, blank=True)
    recomandition_letter3 = models.ImageField(
        upload_to="teacher/job3/", null=True, blank=True)

    image = models.ImageField(
        upload_to="teacher/images", null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.teacher_name
