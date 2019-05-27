from django.contrib import admin
from .models import Profile, Article


@admin.register(Profile)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('user', 'subscription', )
    list_display_links = ('user', )
    search_fields = ('user', 'subscription', )


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_paid_content', )
    list_display_links = ('title', )
    search_fields = ('title', 'description', )




