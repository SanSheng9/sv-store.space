from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe


from .models import *

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Product)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Img)

