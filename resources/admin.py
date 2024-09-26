from django.contrib import admin
from .models import Resource

# Register your models here.
@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('group', 'title', 'description', 'image', 'pdf', 'created_at')
    search_fields = ('group', 'title', 'description')