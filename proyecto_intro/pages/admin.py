from django.contrib import admin
from .models import *

class ChecklistItemAdmin(admin.ModelAdmin):
    list_display = ('elementos', 'fecha', 'user')

    
admin.site.register(UserProfile)
admin.site.register(ChecklistItem,ChecklistItemAdmin)
admin.site.register(News)
admin.site.register(Category)

# Register your models here.
