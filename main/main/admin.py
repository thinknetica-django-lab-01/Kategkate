
from django.contrib import admin
from django.contrib.flatpages.models import FlatPage


class FlatPageAdmin(admin.ModelAdmin):
    model = FlatPage


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
