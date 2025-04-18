from django.contrib import admin
from testApp.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display= ['id','eno', 'ename', 'esal', 'edeg', 'eaddr']
admin.site.register(Employee, EmployeeAdmin)