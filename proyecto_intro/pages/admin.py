from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(ChecklistItem)
admin.site.register(News)
admin.site.register(Category)

# Register your models here.
