#coding: utf-8
from django.shortcuts import render, get_object_or_404
from .models import Rukzak
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from cart.forms import CartAddProductForm

def rukz_product_list(request):
    '''
    product_list method pulling all bags from db
    we also need to create filter to show how many bags we have in Chelyabinsk
    we need two lists of bags: Chelyabinsk_list(1 day delivery time)
                               Ekat_list(3-4 days delivery time)
    in rukz.models.py we have naim method. we look in this method and if we see ##
    this symbol, this bag is in chel_list, other bags are in ekat_list
    '''
    #product_list = Rukzak.objects.all() # all bags list
    #chel_list = Rukzak.objects.all().filter(naim__contains='##') # bags we have in Chelyabinks
    ekat_list = Rukzak.objects.exclude(naim__contains='##') # bags for available for order


    '''
    paginator performing pagination for product_list (captain obviously)
    '''

    paginator = Paginator(product_list, 25) # Show 25 products per page

    page = request.GET.get('page')
    try:
    	products= paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products= paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products= paginator.page(paginator.num_pages)

    return render(request,
                    'rukz/product/rukz_list.html',
                    {'products': products})

def rukz_product_detail(request, id):
    product = get_object_or_404(Rukzak,id=id)
#    cart_product_form = CartAddProductForm()
    return render(request,
                'rukz/product/rukz_detail.html',
                {'product': product})
#                'cart_product_form': cart_product_form})


'''
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                    'shop/product/list.html',
                    {'category': category,
                    'categories': categories,'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product,id=id,
                                        slug=slug,
                                        available=True)
#    cart_product_form = CartAddProductForm()
    return render(request,
                'shop/product/detail.html',
                {'product': product,})
#                'cart_product_form': cart_product_form})
'''