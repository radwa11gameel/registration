from django.contrib import admin

#import apps from models
from products.models import Product, PhoneBrand

# Register your models here.
admin.site.register(Product)
admin.site.register(PhoneBrand)


