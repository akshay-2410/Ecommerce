from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime
from eshop_app.models import *

class Home(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories']=Categories.objects.all()
        context['is_home'] = True
        return context

class Shop(TemplateView):
    template_name = 'shop.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories']=Categories.objects.all()
        context['is_shop'] = True
        return context


class Cart(TemplateView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories']=Categories.objects.all()
        return context
    
class Checkout(TemplateView):
    template_name = 'checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories']=Categories.objects.all()
        return context

class Detail(TemplateView):
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories']=Categories.objects.all()
        return context

class Contact(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories']=Categories.objects.all()
        context['is_contact'] = True
        return context