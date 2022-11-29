from django.contrib import admin
from .models import *
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    list_display= ['id','team_name','project_idea','project_discrapition']
    search_fields = ['team_name',]
admin.site.register(Team, TeamAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display= ['id','name','contact','email','school_name','address','create_time','update_time','is_lead']
    search_fields = ['name',]
admin.site.register(Student, StudentAdmin)