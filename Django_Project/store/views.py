from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from store.models import Product
from store.forms import AddProductForm

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

def add_product(request):

    if request.method == 'POST':
        # print(request.POST)

        form = AddProductForm(request.POST)

        if form.is_valid():
            product = form.save(commit=False)
            # print(request.user)

            # product.is_available = False

            # product.quantity = 100
            product.save()

            return redirect('store:products')

    else:
        form = AddProductForm()

    return render(request, 'add_product.html', {'form': form})

def update_product(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)

    if request.method == 'POST':
        # print(request.POST)

        form = AddProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()

            return redirect('store:product_detail', product_pk=product_pk)

    else:
        form = AddProductForm(instance=product)

    return render(request, 'update_product.html', {'form': form})

def delete_product(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)

    if request.method == 'POST':
        product.delete()
        return redirect('store:products')
    return redirect('store:product_detail', product_pk=product_pk)





















