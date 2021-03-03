"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from shop import views
from django.conf.urls import url, include
from django.contrib import admin
from shop.views import AboutView, ContactView, GoodsListView, ItemDetailView

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('about/', AboutView.as_view()),
    path('contact/', ContactView.as_view()),
    path('goods/', GoodsListView.as_view(), name='goods'),
    path('good/<pk>', ItemDetailView.as_view()),
]
