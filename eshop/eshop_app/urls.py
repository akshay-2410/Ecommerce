from django.urls import path
from eshop_app.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[
    path('',Home.as_view(),name='home'),
    path('shop/', Shop.as_view, name='shop')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 