from django.contrib import admin
from .models import StudyGroup
# Register your models here.
@admin.register(StudyGroup)
class StudyGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'admin')
    search_fields = ('name', 'description', 'admin')

