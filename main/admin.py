from django.contrib import admin
from .models import Cars, CarsImage, AddCar, AddCarImage


class CarsImageAdmin(admin.StackedInline):
    model = CarsImage


@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    inlines = [CarsImageAdmin]

    class Meta:
        model = Cars


@admin.register(CarsImage)
class CarsImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(AddCar)
admin.site.register(AddCarImage)