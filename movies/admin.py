from django.contrib import admin

# Register your models here.
from movies.models import MovieInfo, CensorInfo


class plan(admin.ModelAdmin):
    list_display = ("rating", "certified_by")


class plan1(admin.ModelAdmin):
    list_display = ("title", "year", "description", "poster", "censor_details")


admin.site.register(MovieInfo, plan1)
admin.site.register(CensorInfo, plan)
