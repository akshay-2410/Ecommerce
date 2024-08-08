from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html', next_page='home'), name='login'),
    path('/', LogoutView.as_view(template_name='login.html'), name='logout'),
    path('signup/', SignUp.as_view(), name='signup')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)