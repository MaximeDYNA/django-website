from django.contrib import admin

# Register your models here.
from blog.models import BlogPost

#admin.site.register(BlogPost)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'author',
        'content',
        'published'
    )

    empty_value_display = 'Inconnu'