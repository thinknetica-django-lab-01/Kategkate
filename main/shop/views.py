from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView

from shop.models import ItemInstance


def index(request):
    turn_on_block = False
    # многострочный перенос строки с аргументами
    return render(
        request,
        'index.html',
        {
            'turn_on_block': turn_on_block
        }
    )


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class GoodsListView(ListView):
    template_name = 'goods.html'
    paginate_by = 1
    model = ItemInstance
    context_object_name = 'goods'

    def get_queryset(self):
        tag = self.request.GET.get('tag', None)
        if tag:
            return super(GoodsListView, self).get_queryset().filter(tags__name=tag)
        return super(GoodsListView, self).get_queryset()


class ItemDetailView(DetailView):
    template_name = 'good-detail.html'
    model = ItemInstance
    context_object_name = 'good'
