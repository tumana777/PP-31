from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from store.models import Product
from store.forms import AddProductForm, UpdateProductForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy

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


class ProductListView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
    queryset = Product.objects.filter(is_available=True).select_related('category')
    ordering = ['-created_at']

    # def get_queryset(self):
    #     products = Product.objects.filter(is_available=True).select_related('category')
    #     return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.queryset.count()
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    queryset = Product.objects.filter(is_available=True)
    pk_url_kwarg = 'product_pk'

    # def get_object(self, queryset=None):
    #     product = get_object_or_404(Product, pk=self.kwargs['product_pk'], is_available=True)
    #     return product

class AddProductView(LoginRequiredMixin, CreateView):
    model = Product
    # form_class = AddProductForm
    fields = '__all__'
    template_name = 'add_product.html'
    success_url = '/products'
    login_url = reverse_lazy('user:login')

    # def form_valid(self, form):
    #     """If the form is valid, save the associated model."""
    #     self.object = form.save(commit=False)
    #     self.object.is_available = False
    #     self.object.save()
    #     return super().form_valid(form)

class UpdateProductView(UpdateView):
    model = Product
    form_class = UpdateProductForm
    template_name = 'update_product.html'
    queryset = Product.objects.filter(is_available=True)
    pk_url_kwarg = 'product_pk'

    def get_success_url(self):
        return reverse_lazy('store:product_detail', kwargs={'product_pk': self.object.pk})

class DeleteProductView(DeleteView):
    model = Product
    queryset = Product.objects.filter(is_available=True)
    pk_url_kwarg = 'product_pk'
    success_url = '/products'

class IndexView(TemplateView):
    template_name = 'index.html'



















