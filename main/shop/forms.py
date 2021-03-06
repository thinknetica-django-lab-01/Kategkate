from django.forms import ModelForm
from .models import ItemInstance


class ItemUpdateForm(ModelForm):

    class Meta:
        model = ItemInstance
        fields = ['item', 'price', 'tags']


class ItemCreateForm(ModelForm):

    class Meta:
        model = ItemInstance
        fields = ['item', 'price', 'tags']
