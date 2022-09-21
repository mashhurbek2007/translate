from django.contrib import admin
from .models import TranslatePage

@admin.register(TranslatePage)
class Tranlate(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

