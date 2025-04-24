from django.contrib import admin
from testApp.models import Employee

# Register your models here.
class emp_data(admin.ModelAdmin):
    list_display= ['eno', 'ename', 'email', 'deg']
admin.site.register(Employee, emp_data)