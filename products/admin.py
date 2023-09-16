from django.contrib import admin
from . import models


class ProductImageAdminModel(admin.StackedInline):
    model = models.ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active', 'is_featured' ,'imagecount']
    inlines = [ProductImageAdminModel]
    search_fields = ['slug', 'name', 'pk']
    list_filter = ['is_active', 'is_featured']
    actions = ['make_active', 'make_inactive', 'make_featured', 'make_not_featured']


    fieldsets = (
        ('General Information', {
            'fields': ('name', 'slug', 'description' ,'price' , 'inventory'), 
        }),
        ('Category Status', {
            'fields': ('is_active', 'is_featured')
        }),
    )

    def make_active(self, request, queryset):
        # Custom action to make selected products active
        queryset.update(is_active=True)
    make_active.short_description = "Make selected products active"

    def make_inactive(self, request, queryset):
        # Custom action to make selected products inactive
        queryset.update(is_active=False)
    make_inactive.short_description = "Make selected products inactive"

    def make_featured(self, request, queryset):
        # Custom action to make selected products featured
        queryset.update(is_featured=True)
    make_featured.short_description = "Make selected products featured"

    def make_not_featured(self, request, queryset):
        # Custom action to make selected products not featured
        queryset.update(is_featured=False)
    make_not_featured.short_description = "Make selected products not featured"




    def imagecount(self , obj):
        return obj.images.count()

    # def has_discount(self , obj):
    #     return obj.has_discount()
    imagecount.short_description = "No. of Images"
    # has_discount.short_description = "Discount"


class ProductImageAdmin(admin.ModelAdmin):
    # list_display = ['id', 'product', 'image']
    search_fields = ['product__pk', 'product__name', 'product__slug'] 
    


admin.site.register(models.Product , ProductAdmin)
admin.site.register(models.ProductImage , ProductImageAdmin)