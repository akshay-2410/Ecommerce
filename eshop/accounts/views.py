from django.shortcuts import render
from django.views.generic.edit import CreateView
from accounts.forms import *

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = '/accounts/login/'
    success_message = "%(user)s was updated successfully"