from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.registration_view, name='register'),
    path('donation', views.donation_view, name='donation'),
    path('confirmation', views.ConfirmDonation.as_view(), name='donation-confirmation')
]
