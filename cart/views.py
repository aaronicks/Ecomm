from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

# Create your views here.


def cart_summary(request):

    # get cart
    cart = Cart(request)

    cart_products = cart.get_prod
    return render(request, 'cart_summary.html', {'cart_products':cart_products})


def cart_add(request):
    
    # get the cart
    cart = Cart(request)
    
    # test for post
    if request.POST.get('action') == 'post':
        # get some stuff
        product_id = int(request.POST.get('product_id'))

        # look up product in DB
        product = get_object_or_404(Product, id=product_id)

        # save to session
        cart.add(product=product)


        # get cart quantity
        cart_quantity = cart.__len__()

        # retrn respone
        # response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({'qty: ': cart_quantity})
        return response

def cart_delete(request):
    pass


def cart_update(request):
    pass


