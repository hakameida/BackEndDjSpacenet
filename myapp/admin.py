from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Laptop, LaptopDynamicSpec,
    Computer, ComputerType, ComputerDynamicSpec,
    Accessory, AccessoryType, AccessoryDynamicSpec,
    DollarPrice, Offer, YouTubeLinks
)

# ============ Laptop Admin ============
class LaptopDynamicSpecInline(admin.TabularInline):
    model = LaptopDynamicSpec
    extra = 1
    fields = ('key', 'value')

class LaptopAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_preview', 'price', 'status', 'age', 'cpu', 'gpu', 'ram')
    list_filter = ('status', 'age')
    search_fields = ('name', 'description')
    inlines = [LaptopDynamicSpecInline]
    
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'description', 'price', 'discount', 'age', 'status', 'count')
        }),
        ('Hardware Specs', {
            'fields': ('cpu', 'gpu', 'ram', 'hard', 'screen', 'color', 'os')
        }),
        ('Images', {
            'fields': ('image1', 'image2', 'image3', 'image4', 'image5')
        }),
        ('URLs', {
            'fields': ('url1', 'url2', 'url3', 'url4', 'url5')
        }),
    )
    
    def image_preview(self, obj):
        img_url = None
        for field in ['image1', 'url1', 'image2', 'url2', 'image3', 'url3']:
            val = getattr(obj, field)
            if val:
                img_url = val.url if hasattr(val, 'url') else val
                break
        
        if img_url:
            return format_html(
                '<img src="{}" style="height:100px; border-radius:6px;"/>',
                img_url
            )
        return "No Image"
    image_preview.short_description = "Thumbnail"

# ============ Computer Admin ============
class ComputerDynamicSpecInline(admin.TabularInline):
    model = ComputerDynamicSpec
    extra = 1
    fields = ('key', 'value')

class ComputerAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_preview', 'price', 'status', 'age', 'type')
    list_filter = ('type', 'status', 'age')
    search_fields = ('name', 'description')
    inlines = [ComputerDynamicSpecInline]
    
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'description', 'price', 'discount', 'type', 'age', 'status', 'count')
        }),
        ('Images', {
            'fields': ('image1', 'image2', 'image3', 'image4', 'image5')
        }),
        ('URLs', {
            'fields': ('url1', 'url2', 'url3', 'url4', 'url5')
        }),
    )
    
    def image_preview(self, obj):
        img_url = None
        for field in ['image1', 'url1', 'image2', 'url2', 'image3', 'url3']:
            val = getattr(obj, field)
            if val:
                img_url = val.url if hasattr(val, 'url') else val
                break
        
        if img_url:
            return format_html(
                '<img src="{}" style="height:100px; border-radius:6px;"/>',
                img_url
            )
        return "No Image"
    image_preview.short_description = "Thumbnail"

# ============ Accessory Admin ============
class AccessoryDynamicSpecInline(admin.TabularInline):
    model = AccessoryDynamicSpec
    extra = 1
    fields = ('key', 'value')

class AccessoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_preview', 'price', 'status', 'age', 'type', 'brand')
    list_filter = ('type', 'status', 'age')
    search_fields = ('name', 'description', 'brand')
    inlines = [AccessoryDynamicSpecInline]
    
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'description', 'price', 'discount', 'type', 'age', 'status', 'count')
        }),
        ('Accessory Details', {
            'fields': ('brand', 'model_number', 'compatibility')
        }),
        ('Images', {
            'fields': ('image1', 'image2', 'image3', 'image4', 'image5')
        }),
        ('URLs', {
            'fields': ('url1', 'url2', 'url3', 'url4', 'url5')
        }),
    )
    
    def image_preview(self, obj):
        img_url = None
        for field in ['image1', 'url1', 'image2', 'url2', 'image3', 'url3']:
            val = getattr(obj, field)
            if val:
                img_url = val.url if hasattr(val, 'url') else val
                break
        
        if img_url:
            return format_html(
                '<img src="{}" style="height:100px; border-radius:6px;"/>',
                img_url
            )
        return "No Image"
    image_preview.short_description = "Thumbnail"

# ============ Computer Type Admin ============
class ComputerTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
    )

# ============ Accessory Type Admin ============
class AccessoryTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
    )

# ============ Offer Admin ============
class OfferAdmin(admin.ModelAdmin):
    list_display = ( 'price', 'status', 'product_module')
    list_filter = ('status', 'product_module')
    
    fieldsets = (
        ('Basic Info', {
            'fields': ( 'price', 'status', 'product_module', 'product_id')
        }),
    )

# ============ Dollar Price Admin ============
class DollarPriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'dollar_price')
    
    fieldsets = (
        (None, {
            'fields': ('dollar_price',)
        }),
    )

# ============ YouTube Links Admin ============
class YouTubeLinksAdmin(admin.ModelAdmin):
    list_display = ('id', 'youtubeUrl')
    
    fieldsets = (
        (None, {
            'fields': ('youtubeUrl',)
        }),
    )

# Register all models
admin.site.register(Laptop, LaptopAdmin)
admin.site.register(Computer, ComputerAdmin)
admin.site.register(ComputerType, ComputerTypeAdmin)
admin.site.register(Accessory, AccessoryAdmin)
admin.site.register(AccessoryType, AccessoryTypeAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(DollarPrice, DollarPriceAdmin)
admin.site.register(YouTubeLinks, YouTubeLinksAdmin)