from django.contrib import admin
from django.contrib.auth.models import Group

from.models import Product, Type, Subtype, Order, Client


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'is_published', 'time_update')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    list_editable = ('is_published', 'price')

    # resource_class = BookResource
    fieldsets = (
        ('Общие', {'fields': ('title', 'type', 'price', 'series', 'article', 'width', 'height', 'depth', 'time_update',
                              'time_create', 'photo_file_name', 'is_published', 'description')}),
        ('Частные', {'fields': ('subtype', 'execution_material', 'purpose', 'oven_material')}),
    )

    # эти же поля для отображения должны присутствовать в списке fields
    readonly_fields = ('time_create', 'time_update', 'photo_file_name')

    # обязательно запятую, тк кортеж (если ее не поставить, будет тупо строка)
    list_filter = ('type',)
    # render filtered options only after 1 characters were entered
    filter_input_length = {
        'type': 1,
    }


# первым параметром класс модели, вторым - вспомогаетльный класс
# admin.site.register(Product, ProductAdmin)
admin.site.register(Type)
admin.site.register(Subtype)
admin.site.register(Order)
admin.site.register(Client)
admin.site.unregister(Group)

# меняем названия админ панели
admin.site.site_title = 'NKS'
admin.site.site_header = 'NKS_HEADER'
