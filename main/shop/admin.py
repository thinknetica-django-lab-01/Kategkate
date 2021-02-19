from django.contrib import admin
from .models import Author, Category, Item, ItemInstance

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Item)
admin.site.register(ItemInstance)
