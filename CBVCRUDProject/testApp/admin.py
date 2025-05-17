from django.contrib import admin
from testApp.models import companyModel

# Register your models here.

class companyAdmin(admin.ModelAdmin):
    list_display= ['name', 'location', 'ceo']

admin.site.register(companyModel, companyAdmin)