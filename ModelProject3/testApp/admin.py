from django.contrib import admin
from testApp.models import Teacher

# Register your models here.
class Teacher_List(admin.ModelAdmin):
    list_display= ['id','tno', 'tname', 'sub']

admin.site.register(Teacher, Teacher_List)