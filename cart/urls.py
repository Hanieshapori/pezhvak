from django.urls import path
from . import views
from .views import HomePageView, ShopPageView, AboutPageView, ContactPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('shop/', views.ShopPageView, name='shop'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
]