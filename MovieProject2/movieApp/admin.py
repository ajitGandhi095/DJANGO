from django.contrib import admin
from movieApp.models import MovieModel

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display= ['title', 'hero', 'heroine', 'release']

admin.site.register(MovieModel, MovieAdmin)
