from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('category/', category, name='category'),
    path('blog_view/', blog_view, name='blog-view'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('forms/', forms, name='forms'),
    path('product/', product, name='product'),

]

