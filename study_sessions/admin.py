from django.contrib import admin
from .models import StudySession
# Register your models here.
@admin.register(StudySession)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('group', 'date', 'time', 'topic', 'duration')
    search_fields =('group', 'date', 'time', 'topic', 'duration')
