from django.shortcuts import render, redirect, get_object_or_404
from ongoappfolder.models import HotelName,UserLoginDetails,MerchantDetails
from .models import Cart,CartItem
from django.core.exceptions import ObjectDoesNotExist




# Create your views here.
def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart

def add_cart(request,product_id):
    
    product=HotelName.objects.get(id=product_id)
    print('product ;',product)
   
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
        cart.save(),
    try:
        cart_item=CartItem.objects.get(product=product,cart=cart)
        # if cart_item.quantity < cart_item.product.stock:
        print(cart_item.product.stock)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity+=1
            product.stock=product.stock-cart_item.quantity
            product.save()
        cart_item.active=True    
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(
            product=product,
            quantity= 1 ,
            cart=cart ,
            active= True
        )
        cart_item.save()
    return redirect('cart:cart_detail')


# def add_cart(request,product_id):
#     dish=HotelName.objects.get(id=product_id)
#     try:
#         cart=Cart.objects.get(cart_id=_cart_id(request))
#     except Cart.DoesNotExist:
#         cart = Cart.objects.create(
#             cart_id=_cart_id(request)
#         )
#         cart.save(),
#     try:
#         cart_item=CartItem.objects.get(dish=dish,cart=cart)
#         cart_item.quantity+=1
#         cart_item.save()
#     except CartItem.DoesNotExist:
#         cart_item=CartItem.objects.create(
#             dish=dish,
#             quantity=1,
#             cart=cart
#         )
#         cart_item.save()
#     return redirect('cart:cart_detail')

def cart_detail(request, total=0, counter=0, cart_items=None):
    if request.user.user_type == 'customer':
        data = UserLoginDetails.objects.get(username__username=request.user.username)
    else:
        data = MerchantDetails.objects.get(username__username=request.user.username)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
        request.session['total'] = int(total)
    except ObjectDoesNotExist:
        return render(request, 'cart.html', dict(cart_items=cart_items, total=total, counter=counter, data=data))
    return render(request, 'cart.html', dict(cart_obj=cart, cart_items=cart_items, total=total, counter=counter, data=data))

def cart_remove(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    product=get_object_or_404(HotelName,id=product_id)
    cart_item=CartItem.objects.get(product=product,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')

def full_remove(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(HotelName, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart:cart_detail')



