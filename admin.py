from django.contrib import admin
from .models import ODTTemplate

@admin.register(ODTTemplate)
class TemplateAdmin(admin.ModelAdmin):
    pass


# Register your models here.
