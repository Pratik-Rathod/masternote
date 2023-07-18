from django.contrib import admin
from .models import NotesModel
# Register your models here.

class NotesModelAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "last_edit")

admin.site.register(NotesModel,NotesModelAdmin)
