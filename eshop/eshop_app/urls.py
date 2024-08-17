from django.urls import path
from eshop_app.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[
    path('',Home.as_view(),name='home'),
    path('shop/', Shop.as_view(), name='shop'),
    path('cart/', Cart.as_view(), name='cart'),
    path('checkout/', Checkout.as_view(), name='checkout'),
    path('contact/', Contact.as_view(), name='contact'),
    path('detail/', Detail.as_view(), name='detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 