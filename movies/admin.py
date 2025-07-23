from django.contrib import admin

# Register your models here.
from movies.models import MovieInfo

admin.site.register(MovieInfo)
