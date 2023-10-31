from django.contrib import admin
from .models import Cars, CarsImage, AddCar, AddCarImage, CarParts, Accessories, Problem, Craftsman, Contacts, Fusion, FusionYear


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


class AddCarAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


class AddCarImageAdmin(admin.ModelAdmin):
    list_display = ['post', 'images']


class CarPartsAdmin(admin.ModelAdmin):
    list_display = ['description']
    list_filter = ['value']


class AccessoriesAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['value']


class ProblemAdmin(admin.ModelAdmin):
    list_display = ['text', 'photo']


class CraftsmanAdmin(admin.ModelAdmin):
    search_fields = ['profession']
    list_display = ['name', 'profession', 'number']


class ContactsAdmin(admin.ModelAdmin):
    search_fields = ['el_post']
    list_display = ['el_post', 'text']


admin.site.register(AddCar, AddCarAdmin)
admin.site.register(AddCarImage, AddCarImageAdmin)
admin.site.register(CarParts, CarPartsAdmin)
admin.site.register(Accessories, AccessoriesAdmin)
admin.site.register(Problem, ProblemAdmin)
admin.site.register(Fusion)
admin.site.register(FusionYear)
admin.site.register(Craftsman, CraftsmanAdmin)
admin.site.register(Contacts, ContactsAdmin)


