from django.contrib import admin
from .models import News
# Register your models here.

@admin.register(News)
class FunAdmin(admin.ModelAdmin):
    list_display = ['id','title','photo']