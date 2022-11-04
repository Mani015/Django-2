from django.shortcuts import render

# Create your views here.
def  Toys(request):
    my_product={
    'product1':'iron',
    'product2':'spiderman',
    'product3':'hulk',
    'product4':'remotecar'
    }
    return render(request, 'template/toy.html',my_product)


def  shoes(request):
    my_product={
    'product1':'nike',
    'product2':'adidas',
    'product3':'Reebok',
    'product4':'caterpillar'
    }
    return render(request, 'template/shoe.html',my_product)

def  mobiles(request):
    my_product={
    'product1':'iphone',
    'product2':'one+',
    'product3':'samsung',
    'product4':'oppo'
    }
    return render(request, 'template/product.html',my_product)

def home(request):
    return render(request, 'template/home.html')
