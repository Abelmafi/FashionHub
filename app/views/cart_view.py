from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.db.models import F, Sum
from django.conf import settings
from decimal import Decimal
from ..models.cart import *
from products.models import Product
from ..forms.cart_form import CartForm


@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
   # coupon_form = CouponForm()

    total = cart_items.aggregate(total=Sum(F('quantity') * F('product__price')))['total'] or 0

    context = {'cart_items': cart_items,
            'total': total}
    return render(request, 'cart.html', context)


@login_required
@require_POST
def add_to_cart(request, product_id):
    cart, created = Cart.objects.get_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)

    form = CartForm(request.POST, product=product)
    if form.is_valid():
        quantity = form.cleaned_data['quantity']
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity = quantity
        cart_item.save()
        return JsonResponse({'success': True, 'message': 'Item added to cart'})

    return JsonResponse({'success': False, 'message': 'Invalid form data'})

@login_required
@require_POST
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
    cart_item.delete()
    return JsonResponse({'success': True, 'message': 'Item removed from cart'})


@login_required
@require_POST
def update_cart_item(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)

    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        if quantity:
            cart_item.quantity = int(quantity)
            cart_item.save()
            return JsonResponse({'success': True, 'message': 'Cart item quantity updated.'})
    
    return JsonResponse({'success': False, 'message': 'Invalid request.'})


@login_required
@require_POST
def apply_coupon(request):
    cart, created = Cart.objects.get_or_create(user=request.user)

    coupon_form = CouponForm(request.POST)
    if coupon_form.is_valid():
        code = coupon_form.cleaned_data['code']
        coupon = get_object_or_404(Coupon, code=code)
        if coupon.is_valid():
            cart.coupon = coupon
            cart.save()
            return JsonResponse({'success': True, 'message': 'Coupon applied'})
        else:
            return JsonResponse({'success': False, 'message': 'Coupon is invalid'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid form data'})

