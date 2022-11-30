from django.contrib import admin
from .models import Tag, Topic

# Register your models here.




@admin.register(Topic)
class AdminTagRegister(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Tag)
class AdminTagRegister(admin.ModelAdmin):
    list_display = ['name']
    

    