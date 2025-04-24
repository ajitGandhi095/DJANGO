from django.contrib import admin
from jobApp.models import HYD
from jobApp.models import PUNE
from jobApp.models import BANGALORE

# Register your models here.
class dis_data(admin.ModelAdmin):
    list_display= ['date', 'company', 'roll', 'eligibility', 'address', 'email', 'phonenumber']

admin.site.register(HYD, dis_data)
admin.site.register(PUNE, dis_data)
admin.site.register(BANGALORE, dis_data)