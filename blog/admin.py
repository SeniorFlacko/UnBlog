from django.contrib import admin

# Register your models here.
from . import models

class EntryAdmin(admin.ModelAdmin):
    list_display = ("title", "created")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(models.Entry, EntryAdmin)