from django.shortcuts import render
from django.views.generic import TemplateView
#from django.views.generic.edit import CreateView

from .models import Product


class HomePageView(TemplateView):
    template_name = 'home.html'


def ShopPageView(request):
        all_products = Product.objects.all()
        return render(request, 'shop.html', {'products': all_products})


class ContactPageView(TemplateView):
    template_name = 'contact.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'

class LoginPageView(TemplateView):
    template_name = 'login.html'

class LogoutPageView(TemplateView):
    template_name = ' logout.html'
