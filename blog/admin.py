from django.contrib import admin
from .models import Post, CateGory


class CatGoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'position', 'slug', 'status', 'parent')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['parent__id', 'position']



admin.site.register(CateGory, CatGoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'j_published', 'updated', 'status', 'category_to_str', 'number_post')
    list_filter = ('published', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug':('title',)}
    ordering = ['-status']


    def category_to_str(self, obj):
        return ', '.join([category.title for category in obj.category_published()])

    category_to_str.short_description = 'دسته بندی'


admin.site.register(Post, PostAdmin)