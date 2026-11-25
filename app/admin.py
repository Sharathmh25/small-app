from django.contrib import admin
from .models import Profile,Product
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['id','name','image','about','email','skills']
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','product_name','product_description','category']