from django.contrib import admin
from formApp.models import StudentModel

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display= ['name', 'rollno', 'marks']

admin.site.register(StudentModel,StudentAdmin)