from django.contrib import admin
from . models import *

# Register your models here.

class AppInfoAdmin(admin.ModelAdmin):
    list_display = ['id']
    
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['id', 'type', 'name', 'img', 'price', 'uploaded']

admin.site.register(Appinfo, AppInfoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Size)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Contact)
admin.site.register(Customer)

