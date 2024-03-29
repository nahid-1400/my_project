from django.contrib import admin
from .models import Post, CateGory, IPAddress, Slider, Hashtag


@admin.action(description='فعال کردن دسته بندی')
def make_active(self, request, queryset):
    row_update = queryset.update(status='True')
    self.message_user(request, ('%s %s' % (row_update, 'دسته بندی فعال شد')))

@admin.action(description='غیر فعال کردن دسته بندی')
def make_disable(self, request, queryset):
    row_update = queryset.update(status='False')
    self.message_user(request, ('%s %s' % (row_update, 'دسته بندی غیر فعال شد')))

class CatGoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'position', 'slug', 'status', 'parent')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['parent__id', 'position']
    actions = [make_active, make_disable]



admin.site.register(CateGory, CatGoryAdmin)


# admin.site.disable_action('delete_selected')

@admin.action(description='انتشار مقالات')
def make_published(self, request, queryset):
    rows_update = queryset.update(status='p')
    self.message_user(request, ('%s %s' % (rows_update,  ' مقاله منتشر شد')))

@admin.action(description=' پیش نویس مقالات')
def make_draft(self, request, queryset):
    rows_update = queryset.update(status='d')
    self.message_user(request, ('%s %s' % (rows_update, ' مقاله پیش نویس شد')))


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', 'author', 'j_published', 'updated', 'is_special', 'status', 'category_to_str', 'number_post')
    list_filter = ('published_time', 'status', 'author')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-status']
    actions = [make_published, make_draft]






admin.site.register(Post, PostAdmin)
admin.site.register(Slider)
admin.site.register(Hashtag)
admin.site.register(IPAddress)