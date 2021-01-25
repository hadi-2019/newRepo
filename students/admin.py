from django.contrib import admin

# Register your models here.
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('kankor_id', 'first_name', 'last_name',
                    'kankor_score', 'student_registration_date')
    list_display_links = ('kankor_id', 'first_name')
    search_fields = ('first_name', )
    list_per_page = 20


admin.site.register(Student, StudentAdmin)
