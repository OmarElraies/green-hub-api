from django.contrib import admin

# Register your models here.
from .models import Plants, Category, Places

admin.site.register(Plants)
admin.site.register(Category)
admin.site.register(Places)
