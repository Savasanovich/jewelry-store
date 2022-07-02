from django.shortcuts import render
from .models import Product , Category
from .forms import ProductForm
# Create your views here.

def index (request):


    forms = ProductForm()
    ctx = {
        'forms': forms,
    }

    return render(request, 'index.html', ctx)

def about (request):

    return render(request, 'about.html', {})

def blog (request) :

    return render(request, 'blog.html', {})

def blog_view (request) :

    return render(request, 'blog_view.html' , {})

def cart (request) :

    return render(request, 'cart.html', {})

def category (request):

    return render(request, 'request.html', {})

def checkout(request):

    return render(request, 'checkout.html', {})

def forms(request):

    return render(request, 'forms.html', {})

def product(request):

    return render(request, 'product.html', {})


