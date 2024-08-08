from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime
from eshop_app.models import *

class Home(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories']=Categories.objects.all()
        return context

class Shop(TemplateView):
    template_name = 'shop.html'
