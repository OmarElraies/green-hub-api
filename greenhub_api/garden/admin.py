from django.contrib import admin

# Register your models here.
from .models import Plants, Category, Places, SubCategory

admin.site.register(Plants)
admin.site.register(Category)
admin.site.register(Places)
admin.site.register(SubCategory)
