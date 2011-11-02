from django.contrib import admin
from apps.data.models import Entry

class EntryAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'created', 'updated', 'published')

admin.site.register(Entry)
