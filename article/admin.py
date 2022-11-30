from django.contrib import admin


from .models import Post


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ["author", "topic", 'tag', 'category', 'pub_date']
    prepopulated_fields = {"slug": ['title', ]}
    search_fields = ['category', 'tag']
    list_filter = ['category', 'tag', 'author']




