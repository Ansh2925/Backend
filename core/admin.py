from django.contrib import admin
from core.models import Drinks, DrinksCategory, Menu, Customer, Vehicle

# Register your models here.
# Model registration using admin.site.register() is required to access the model from the admin user interface.
admin.site.register(Drinks)
admin.site.register(DrinksCategory)
admin.site.register(Menu)
admin.site.register(Customer)
admin.site.register(Vehicle)