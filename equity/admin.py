from django.contrib import admin

# Register your models here.

from equity.models import Securities, SecuritySelectionModels, ClassificationNames, Exchanges, Countries, \
    AllocationModels, \
    Currencies

admin.site.register(Securities)
admin.site.register(SecuritySelectionModels)
admin.site.register(ClassificationNames)
admin.site.register(Exchanges)
admin.site.register(Countries)
admin.site.register(AllocationModels)
admin.site.register(Currencies)
