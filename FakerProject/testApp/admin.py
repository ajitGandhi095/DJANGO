from django.contrib import admin
from testApp.models import STUDENT
# Register your models here.
class studentAdmin(admin.ModelAdmin):
    list_display= ['rollno', 'name', 'dob', 'email', 'phonenumber', 'marks', 'address']

admin.site.register(STUDENT, studentAdmin)