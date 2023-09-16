from django.contrib import admin
from .models import Category
# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
    list_display= ['id' , 'name' , 'slug' , 'is_active', 'is_featured']
    list_filter = ['is_active', 'is_featured']
    search_fields= ['slug', 'name' , 'pk']
    actions = ['mark_as_active', 'mark_as_inactive']

    fieldsets = (
        ('General Information', {
            'fields': ('name', 'slug', 'description', 'image')
        }),
        ('Category Status', {
            'fields': ('is_active', 'is_featured')
        }),
    )

    def mark_as_active(self, request, queryset):
        queryset.update(is_active=True)

    def mark_as_inactive(self, request, queryset):
        queryset.update(is_active=False)

    mark_as_active.short_description = "Mark selected categories as active"
    mark_as_inactive.short_description = "Mark selected categories as inactive"




    # def product_count(self , obj):
    #     return obj.product_set.count()

    # product_count.short_description = "Number of products"

    
admin.site.register(Category, CategoryAdmin)