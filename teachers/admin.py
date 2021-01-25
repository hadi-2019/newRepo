from django.contrib import admin
from .models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'teacher_name', 'last_name',
                    'birth_year', 'status')
    list_display_links = ('id', 'teacher_name')
    search_fields = ('teacher_name', )
    list_per_page = 20


admin.site.register(Teacher, TeacherAdmin)
