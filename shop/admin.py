from django.contrib import admin

# Register your models here.
from .models import Product
from .models import Contact
from .models import icon
from .models import SpecificBanner


admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(icon)
admin.site.register(SpecificBanner)



