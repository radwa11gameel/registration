from django.shortcuts import render


from products.models import Product

from django.db.models import Q
import os
from django.core.mail import send_mail

# Create your views here.


def homepage(request):
    query = request.GET.get('query', None)
    if query:
        products = Product.objects.filter(Q(name__icontains=query) |
                                          Q(brand__brandName__icontains=query)
                                          ).distinct()
    else:
        # retrieve all objects of Product class
        products = Product.objects.all()
        products = products.order_by('-id')

    showitems = {
        'products': products,
        'title': 'Homepage'
    }
    return render(request, 'homepage.html', context=showitems)

def detail(request, id):
    product = Product.objects.filter(id=id).first()
    details = {
        'product': product,
        'title': product.name,
    }
    return render(request, 'details.html', context=details)

def email(request, id):
    product = Product.objects.filter(id=id).first()
    receipient = request.POST.get('email', None)
    if receipient:
        subject = product.fullname()
        message = '''
        Hey, Thanks for checking out our website.
        You requested to send details of phone to your mail
        so here are details
        BRAND: {}
        MODEL:{}
        PRICE:{}
        Thanks for visiting us. Wish to see you again.
        '''.format(product.brand.brandName, product.name, product.price, product.screen)
        from_email = os.environ.get('email')
        receipient_list = [receipient]
        send_mail(subject, message, from_email,
                  receipient_list, fail_silently=False)
        return detail(request, id)
    else:
        return homepage(request)
