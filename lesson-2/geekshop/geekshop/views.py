from django.shortcuts import render

# Create your views here.
def index(request):
    contex = {
        'date': '2022',
        'header': True,
        'user_firstname': 'Ivan',
        'user_secondname': 'Ivanov',
    }

    return render(request,'geekshop/index.html', contex)


def contacts(request):
    return render(request,'geekshop/contact.html')