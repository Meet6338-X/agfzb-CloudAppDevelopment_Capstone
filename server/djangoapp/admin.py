"""Django admin configuration for the car make and car model models."""
from django.contrib import admin

from .models import CarMake, CarModel


# CarModelInline class
class CarModelInline(admin.StackedInline):
    """Show the car models of a car make on the car make admin page."""

    model = CarModel
    extra = 1


# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    """Admin configuration of the car models."""

    fields = ['car_make', 'name', 'dealer_id', 'model_type', 'year']
    list_display = ['name', 'car_make', 'dealer_id', 'model_type', 'year']
    search_fields = ['name', 'car_make__name']
    list_filter = ['car_make', 'dealer_id', 'model_type', 'year']


# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    """Admin configuration of the car makes, including their car models."""

    fields = ['name', 'description']
    list_display = ['name', 'description']
    search_fields = ['name']
    inlines = [CarModelInline]


# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
