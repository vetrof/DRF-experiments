from django.contrib import admin

from product_list.models import Food, Category


# Register your models here.
class FoodAdminView(admin.ModelAdmin):
    list_display = ('name', 'intro', 'cat', 'id')
    search_fields = ('name', 'intro')
    list_display_links = ('name', 'intro')
    ordering = ('-id',)





admin.site.register(Food, FoodAdminView)
admin.site.register(Category)

