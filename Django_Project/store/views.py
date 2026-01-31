from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from store.models import Product

# def index(request):
#     return HttpResponse('<h1>Hello, world.</h1>')
#
# def about(request):
#     return HttpResponse('This is about page')

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def products(request):
    all_products = Product.objects.filter(is_available=True).select_related('category')

    context = {'products': all_products, 'count': all_products.count()}

    return render(request, 'products.html', context)

def products_json(request):
    products = Product.objects.all()
    return JsonResponse({ 'products': list(products.values())})

def product_detail(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    return render(request, 'product_detail.html', {'product': product})
































