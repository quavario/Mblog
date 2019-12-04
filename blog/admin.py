from django.contrib import admin

# Register your models here.
from blog.models import Post, Config


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'create_date', 'status']
    list_display_links = ['title', 'edit']
    list_display = ['id', 'title', 'create_date', 'username', 'edit']
    exclude = ['create_by', 'update_by', 'order', 'status']

    # 每页个数
    list_per_page = 10

    def save_model(self, request, obj, form, change):
        if obj.id is None:
            obj.create_by = request.user.id
        obj.update_by = request.user.id
        super().save_model(request, obj, form, change)


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    # search_fields = ['title', 'create_date', 'status']
    list_display_links = []
    list_display = ['name', 'value', 'type']

