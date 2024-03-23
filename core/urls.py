from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

from .forms import LoginForm
app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('terms/', views.terms, name='terms'),
    path('signup/', views.signup, name='signup'),

    # It will use the custom login form that django will use to authenticate the user
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'), ]





