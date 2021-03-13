from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save
from django.dispatch import receiver


class FlatPageAdmin(admin.ModelAdmin):
    model = FlatPage


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
