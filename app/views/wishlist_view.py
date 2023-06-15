from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
# from ..models.wishlist import Wishlist
from products.models import Product

@login_required
def add_to_wishlist(request, product_id):
    """
    View to add a product to user's wishlist
    """
    product = Product.objects.get(id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist_item.products.add(product)
    if created:
        message = f"{product.name} has been added to your wishlist!"
    else:
        message = f"{product.name} is already in your wishlist!"
    data = {'message': message, 'wishlist_item': wishlist_item.to_dict()}
    return JsonResponse(data)


@login_required
def wishlist(request):
    """
    View to display user's wishlist
    """
    wishlist = Wishlist.objects.get(user=request.user)
    # wishlist = Wishlist.objects.get(pk=wishlist_id)
    products = wishlist.products.all()

    context = {
        'wishlist': wishlist,
        'products': products
    }


    return render(request, 'wishlist.html', context)


@login_required
def remove_from_wishlist(request, product_id):
    """
    View to remove a product from user's wishlist
    """
    wishlist = Wishlist.objects.get(user=request.user)
    product = Product.objects.get(id=product_id)
    wishlist.products.remove(product)
    message = f"{wishlist.products.name} has been removed from your wishlist!"
    data = {'message': message}
    return JsonResponse(data)
