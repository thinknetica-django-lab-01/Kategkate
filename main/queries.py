from shop.models import Category, Item, ItemInstance

b = Category(name='Milk Burenka with 3,3% fat', help_text='Milk')
b.save()

b = Category(name='Cheese Gauda with 60% fat', help_text='Cheese')
b.save()


Item.summary.filter(headline__startswith='Analogue')
ItemInstance.status.filter(blank=True)
