from django.contrib import admin
from testApp.models import Teacher

# Register your models here.
class Teacher_list(admin.ModelAdmin):
    list_display= ['tno', 'tname', 'sub', 'sal']

admin.site.register(Teacher, Teacher_list)