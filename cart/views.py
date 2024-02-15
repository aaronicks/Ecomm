from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

# Create your views here.


def cart_summary(request):

    # get cart
    cart = Cart(request)

    cart_products = cart.get_prod
    quantities = cart.get_quants
    totals = cart.cart_total()


    context = {
        'cart_products': cart_products, 
        'quantities': quantities,
        'totals': totals
        }
    return render(request, 'cart_summary.html', context)


def cart_add(request):
    
    # get the cart
    cart = Cart(request)
    
    # test for post
    if request.POST.get('action') == 'post':
        # get some stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        # look up product in DB
        product = get_object_or_404(Product, id=product_id)

        # save to session
        cart.add(product=product, quantity=product_qty)  #quantity coming from cart.py


        # get cart quantity
        cart_quantity = cart.__len__()

        # retrn respone
        # response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({'qty': cart_quantity})
        return response

def cart_delete(request):
    
    # grab the cart
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        # get stuff
        product_id = int(request.POST.get('product_id'))
       
        # call the delete function
        cart.delete(product=product_id)

        response = JsonResponse({'product':product_id})
        return response


def cart_update(request):
    # get the cart
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        # get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        # update our cart
        cart.update(product=product_id, quantity=product_qty)
        response = JsonResponse({'qty':product_qty}) 
        return response
        

        


