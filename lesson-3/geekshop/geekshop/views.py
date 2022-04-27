from django.shortcuts import render

# Create your views here.
from mainapp.models import Product


def index(request):
    products = Product.objects.all()[:4]
    contex = {
        'title': 'главная',
        'products':products,

        'date': '2022',
        'header': True,
        'user_firstname': 'Ivan',
        'user_secondname': 'Ivanov',
    }

    return render(request,'geekshop/index.html', contex)


def contacts(request):
    return render(request,'geekshop/contact.html')