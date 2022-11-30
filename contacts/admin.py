from django.contrib import admin
from .models import Subscription, Contact, Comment
# Register your models here.



def make_post_valid(modelname, request, queryset):
    queryset.update(is_valid=True)
    
make_post_valid.shortdescription = "Make Selected Valid"



@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['email']
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'pub_date']
    list_filter = ['email', 'is_responded']
    search_fields = ['email', 'pub_date']
    
    
    
@admin.register(Comment)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'pub_date', 'is_valid']
    actions = [make_post_valid, ]