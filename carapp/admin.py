from django.contrib import admin
from .models import car,Brand
# Register your models here.
admin.site.register(car)

class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','slug']
admin.site.register(Brand,BrandAdmin)