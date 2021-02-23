from shop.models import Category, Item, ItemInstance

bulk = Category(name='Milk Burenka with 3,3% fat', help_text='Milk')
bulk.save()

bulk = Category(name='Cheese Gauda with 60% fat', help_text='Cheese')
bulk.save()


Item.summary.filter(headline__startswith='Analogue')
ItemInstance.status.filter(blank=True)
