from  django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.http import JsonResponse,Http404
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core import serializers
from django.core.serializers import serialize
from django.template.loader import render_to_string
from .forms import CustomerRegistrationForms , CheckoutAddressForm

import requests
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
# from payoneer_sdk import PayoneerClient
# import payoneer_sdk


from django.views import View
from .forms import CustomerAddress,CustomerRegistrationForms,LoginForm,MyPasswordResetForm
from django.contrib import messages
from django.contrib.auth import authenticate , login,logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import *

# ==================================================Base_View_for_common==================================================
class BaseViewMixin(object):
    def get_common_context(self):
        common_context = {
            'cartheadings': cartheading.objects.all().order_by('id'),
            'Empty': ifEmpty.objects.all().order_by('id'),
            'items': items.objects.all().order_by('id'),
            'OptionCarts': OptionCart.objects.all().order_by('id'),
            'warnings': warning.objects.all().order_by('id'),
            'footercarts': footercart.objects.all().order_by('id'),
            'wishlistheadings': wishlistheading.objects.all().order_by('id'),
            'Optionwishlists': Optionwishlist.objects.all().order_by('id'),
            'EmptyWishlists': EmptyWishlist.objects.all().order_by('id'),
            'searching': search.objects.all().order_by('id'),
            'QuickSearching': QuickSearch.objects.all().order_by('id'),
            'OptionSearching': OptionSearch.objects.all().order_by('id'),
            'account': account.objects.all().order_by('id'),
            'footers': footer.objects.all().order_by('id'),
            'column1s': column1.objects.all().order_by('id'),
            'column2s': column2.objects.all().order_by('id'),
            'column3s': column3.objects.all().order_by('id'),
            'column4s': colunm4.objects.all().order_by('id'),   
            'wishlists':wishlists.objects.all().select_related('productes'),
            'user_cart':User_Cart.objects.all().select_related('product'),   
        }
        return common_context
    
# ==================================================BaseView==================================================
class BaseView(BaseViewMixin, View):
    template_name = 'app/base.html'

# ==================================================HomeView==================================================
# @login_required(login_url='login')
class HomeView(BaseView):
    
    def get(self, request):
        common_context = self.get_common_context()
        sliderone = slider1.objects.all().order_by('id')
        slidertwo = slider2.objects.all().order_by('id')
        handpickeds = handPicked_product.objects.all().order_by('id')
        banner_body = banner.objects.all().order_by('id')
        blogs = Blog.objects.all().order_by('id')
        instaPics = instaPic.objects.all().order_by('id')
        discount_offers = discount_offer.objects.all().order_by('id')
        formtwo = CustomerRegistrationForms() 
        formthree = LoginForm()  
        formfour = MyPasswordResetForm()  
        totalwishlist = 0
        if request.user.is_authenticated:
            totalwishlist = wishlists.objects.filter(user=request.user).values('productes').distinct().count()
            totalwishlist = int(totalwishlist)
        totalcart = 0
        if request.user.is_authenticated:
            totalcart = User_Cart.objects.filter(user=request.user).values('product').distinct().count()
            totalcart = int(totalcart)
        
        context = {
            **common_context,
            'sliderone': sliderone,
            'slidertwo': slidertwo,
            'handpickeds': handpickeds,
            'banner_body': banner_body,
            'blogs': blogs,
            'instaPics': instaPics,
            'discount_offers': discount_offers,
            'formtwo': formtwo,  
            'formthree': formthree,
            'formfour': formfour,
            'totalwishlist':totalwishlist,
            'totalcart':totalcart,
        }
        return render(request,'app/home.html', context)

# ==================================================Shop_Page==================================================
# @login_required(login_url='login')
class ShopView(BaseView):
    def get(self, request):
        common_context = self.get_common_context()
        shop_offers = shop_offer.objects.all().order_by('id')
        filter_products = filter_product.objects.all().order_by('id')
        handpickeds = handPicked_product.objects.all().order_by('id')
        formtwo = CustomerRegistrationForms() 
        formthree = LoginForm()  
        formfour = MyPasswordResetForm() 
        totalwishlist = 0
        if request.user.is_authenticated:
            totalwishlist = wishlists.objects.filter(user=request.user).values('productes').distinct().count()
            totalwishlist = int(totalwishlist)
        totalcart = 0
        if request.user.is_authenticated:
            totalcart = User_Cart.objects.filter(user=request.user).values('product').distinct().count()
            totalcart = int(totalcart)
        context = {
            **common_context,
            'shop_offers': shop_offers,
            'filter_products': filter_products,
            'formtwo': formtwo,  
            'formthree': formthree,
            'formfour': formfour,
            'totalwishlist':totalwishlist,
            'totalcart':totalcart,
            'handpickeds':handpickeds
        }
        return render(request, 'app/shopfilter.html', context)

# ==================================================Blog_Page==================================================
# @login_required(login_url='login')
class BlogView(BaseView):
    def get(self, request):
        common_context = self.get_common_context()
        blogLists = blogList.objects.all().order_by('id')
        categories = catogery.objects.all().order_by('id')
        Latest_Posts = Latest_Post.objects.all().order_by('id')
        Tag = Tags.objects.all().order_by('id')
        formtwo = CustomerRegistrationForms() 
        formthree = LoginForm()  
        formfour = MyPasswordResetForm() 
        totalwishlist = 0
        if request.user.is_authenticated:
            totalwishlist = wishlists.objects.filter(user=request.user).values('productes').distinct().count()
            totalwishlist = int(totalwishlist)
        totalcart = 0
        if request.user.is_authenticated:
            totalcart = User_Cart.objects.filter(user=request.user).values('product').distinct().count()
            totalcart = int(totalcart)
        context = {
            **common_context,
            'blogLists': blogLists,
            'categories': categories,
            'Latest_Posts': Latest_Posts,
            'Tag': Tag,
            'formtwo': formtwo,  
            'formthree': formthree,
            'formfour': formfour,
            'totalwishlist':totalwishlist,
            'totalcart':totalcart,
        }
        return render(request, 'app/bloglist.html', context)

# ==================================================Contact_Page==================================================
# @login_required(login_url='login')
def contact_view(request):
    template_name = 'app/contact.html'

    base_view_mixin = BaseViewMixin() 
    common_context = base_view_mixin.get_common_context() 
    formtwo = CustomerRegistrationForms() 
    formthree = LoginForm()  
    formfour = MyPasswordResetForm() 
    
    if request.method == 'POST':
        formone = CustomerAddress(request.POST)
        if formone.is_valid():
            formone.save()
    else:
        formone = CustomerAddress()
    totalwishlist = 0
    if request.user.is_authenticated:
        totalwishlist = wishlists.objects.filter(user=request.user).values('productes').distinct().count()
        totalwishlist = int(totalwishlist)
    totalcart = 0
    if request.user.is_authenticated:
        totalcart = User_Cart.objects.filter(user=request.user).values('product').distinct().count()
        totalcart = int(totalcart)
    context = {
        **common_context,
        'contacthHeading': contact_heading.objects.all().order_by('id'),
        'formone': formone,
        'Addres': Address.objects.all().order_by('id'),
        'GetTech': GetIntoTech.objects.all().order_by('id'),
        'formtwo': formtwo,  
        'formthree': formthree,
        'formfour': formfour,
        'totalwishlist':totalwishlist,
        'totalcart':totalcart,
    }
    return render(request, template_name, context)

# ==================================================Checkout==================================================
class Checkout(BaseView):
    def get(self, request):
        template_name = 'app/checkout.html'
        base_view_mixin = BaseViewMixin()
        common_context = self.get_common_context()
        formtwo = CustomerRegistrationForms()
        formthree = LoginForm()
        formfour = MyPasswordResetForm()
        totalwishlist = 0
        totalAmount = 0
        amount = 0
        totalcart = 0
        shipping_charges = 90.0

        if request.user.is_authenticated:
            totalwishlist = wishlists.objects.filter(user=request.user).values('productes').distinct().count()
            totalwishlist = int(totalwishlist)
            totalcart = User_Cart.objects.filter(user=request.user).values('product').distinct().count()
            totalcart = int(totalcart)
            cart = User_Cart.objects.filter(user=request.user)
            amount = sum(item.total_cost for item in cart)
            totalAmount = amount + shipping_charges

        form = CheckoutAddressForm()

        context = {
            **common_context,
            'formtwo': formtwo,
            'formthree': formthree,
            'formfour': formfour,
            'totalwishlist': totalwishlist,
            'totalcart': totalcart,
            'totalAmount': totalAmount,
            'amount': amount,
            'form': form
        }

        return render(request, 'app/checkout.html', context)

    def post(self, request):
        form = CheckoutAddressForm(request.POST)
        totalwishlist = 0
        totalAmount = 0
        amount = 0
        totalcart = 0
        shipping_charges = 90.0

        if request.user.is_authenticated:
            totalwishlist = wishlists.objects.filter(user=request.user).values('productes').distinct().count()
            totalwishlist = int(totalwishlist)
            totalcart = User_Cart.objects.filter(user=request.user).values('product').distinct().count()
            totalcart = int(totalcart)
            cart = User_Cart.objects.filter(user=request.user)
            amount = sum(item.total_cost for item in cart)
            totalAmount = amount + shipping_charges

        if form.is_valid():
            fname = form.cleaned_data.get('fname')
            lname = form.cleaned_data.get('lname')
            email = form.cleaned_data.get('email')
            region = form.cleaned_data.get('region')
            address = form.cleaned_data.get('address')
            apartment = form.cleaned_data.get('apartment')
            town = form.cleaned_data.get('town')
            postcode = form.cleaned_data.get('postcode')
            country = form.cleaned_data.get('country')
            phoneNo = form.cleaned_data.get('phoneNo')
            OrderNote = form.cleaned_data.get('OrderNote')

            if not fname or not lname or not email or not address or not postcode or not phoneNo:
                context = {'error': 'Please fill in required fields.'}
                return JsonResponse(context)

            if request.user.is_authenticated:
                checkout_address = CheckoutAddress(
                    user=request.user if request.user.is_authenticated else None,
                    fname=fname,
                    lname=lname,
                    email=email,
                    region=region,
                    address=address,
                    apartment=apartment,
                    town=town,
                    postcode=postcode,
                    country=country,
                    phoneNo=phoneNo,
                    OrderNote=OrderNote
                )
                checkout_address.save()

                new_order = order(user=request.user, total_amount=totalAmount, payment_method='Cash on Delivery')
                new_order.save()

                cart = User_Cart.objects.filter(user=request.user)
                for cart_item in cart:
                    order_item = orderItem(order_no=new_order, product=cart_item.product, quantity=cart_item.quantity)
                    order_item.save()
                    cart_item.delete()

                totalAmount = 0.0

        context = {
            'totalwishlist': totalwishlist,
            'totalcart': totalcart,
            'totalAmount': totalAmount,
            'amount': amount,
            'form': form
        }

        return render(request, 'app/checkout.html', context)


# ==================================================Sign_Up==================================================
def customerRegistrationView(request):
    if request.method == 'POST':
        try:
            uname = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            
            if password1 != password2:
                messages.error(request, 'Confirm Password is not matching!')
            else:
                my_user = User.objects.create_user(username=uname, email=email, password=password1)
                my_user.save()
                return redirect('home')
        except IntegrityError:
            messages.error(request, 'Username already exists. Please choose a different username.')
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
    context = {}
    return render(request, 'includeFiles/SignUp.html', context)

# ==================================================Login==================================================
def LoginView(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(request, username=username,password=pass1)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username Or Password is incorrect ')
        
    context ={}
    return render(request, 'includeFiles/login.html', context)

# ==================================================Logout==================================================
def logoutUser(request):
    logout(request)
    return redirect('home')
# ==================================================Password_Reset==================================================
class MyPasswordResetView(View):
    def get(self, request):
        formfour = MyPasswordResetForm()
        return render(request, 'includeFiles/recovery.html', {'formfour': formfour})
    
    def post(self, request):
        formfour = MyPasswordResetForm(request.POST)
        if formfour.is_valid(): 
            formfour.save()
        else:
            formfour = MyPasswordResetForm()
        return render(request, 'includeFiles/recovery.html', {'formfour': formfour})
# ==================================================Add_To_Wishlist==================================================
# @login_required(login_url='login')

def addtowishlist(request):
    if not request.user.is_authenticated:
        return JsonResponse({"bool": False})

    item_id = int(request.GET.get('id'))
    wishlist_quantity = int(request.GET.get('quantity',1))
    print(f"wishlist quantity is : {wishlist_quantity}")
    if item_id:
        try:
            product = handPicked_product.objects.get(id=item_id)
            wishlist_item, created = wishlists.objects.get_or_create(productes=product,user=request.user,defaults={'quantity': wishlist_quantity})
            if not created:
                
                context = {"bool": False}
                return JsonResponse(context)
            
            context = {"bool": True}
            return JsonResponse(context)

        except ObjectDoesNotExist:
            context = {"bool": False, "text": 'item not found'}
            return JsonResponse(context)
    else:
        context = {"bool": False}
        return JsonResponse(context)

# ==================================================Delete_from_Wishlist==================================================
@login_required(login_url='login')
def deleteFromWishlist(request):
    pid = request.GET.get('id')  

    wishlist = wishlists.objects.filter(user=request.user)
    product = get_object_or_404(wishlists, id=pid)
    product.delete()

    context = {
        "bool": True,
        "wishlist": wishlist,
    }

    wishlist_json = serializers.serialize('json', wishlist)
    data = render_to_string("includeFiles/wishlist.html", context)
    return JsonResponse({"data": data, "products": wishlist_json})

# ======================================add_to_cart=============================================================
def addtocart(request):
    cart_id = request.GET.get('id')
    item_quantity = request.GET.get('item_quantity')

    # Set a default context value
    context = {"bool": False, "totalamount": 0}

    if cart_id:
        try:
            cart_id = int(cart_id)
            item_quantity = int(item_quantity)

            product = handPicked_product.objects.get(id=cart_id)
            cart_count = User_Cart.objects.filter(user=request.user, product=product)

            if cart_count:
                cart_count = cart_count.first()
                context = {"bool": False, "cart_count": cart_count.quantity}
            else:
                cart_item = User_Cart.objects.create(user=request.user, product=product, quantity=item_quantity)
                if cart_item:
                    cart_item.save()
                    wishlists.objects.filter(user=request.user, productes=product).delete()
                    context = {"bool": True, "cart_item": cart_item.quantity}

        except ObjectDoesNotExist:
            context = {"bool": False, "text": 'Object not found'}

    return JsonResponse(context)


# ==================================================Delete_from_Cart==================================================
@login_required(login_url='login')
def deleteFromCart(request):
    pid = request.GET.get('id')  
    product = get_object_or_404(User_Cart, id=pid)
    
    product.delete()

    cart = User_Cart.objects.filter(user=request.user)
    
    cart_json = serialize('json', cart)
    context = {
        "bool": True,
        "User_Cart": cart,
    }
    data = render_to_string("includeFiles/cart.html", context)
    return JsonResponse({"data": data, "products": cart_json})

# ==================================================Price==================================================================

def cart_price(request):
    cart = User_Cart.objects.filter(user=request.user)
    amount = sum(item.total_cost for item in cart)
    shipping_charges = 90.0
    totalAmount = amount + shipping_charges
    return JsonResponse({'amount': amount, 'totalAmount': totalAmount})
    

# ==================================================plus_cart_price==================================================================


def plus_cart_price(request):
    if request.method == 'GET':
        id = request.GET['id']
        cart = User_Cart.objects.get(Q(product=id) & Q(user=request.user))
        cart.quantity += 1
        cart.save()

        cart_items = User_Cart.objects.filter(user=request.user)
        amount = cart.total_cost
        shipping_charges = 90.0
        totalAmount = sum(item.total_cost for item in cart_items) + shipping_charges

        return JsonResponse({'quantity': cart.quantity, 'amount': amount, 'totalAmount': totalAmount})


# ==================================================minus_cart_price==================================================================

def minus_cart_price(request):
    if request.method == 'GET':
        id = request.GET['id']
        cart = User_Cart.objects.get(Q(product=id) & Q(user=request.user))
        cart.quantity -= 1
        cart.save()

        cart_items = User_Cart.objects.filter(user=request.user)
        amount = cart.total_cost
        shipping_charges = 90.0
        totalAmount = sum(item.total_cost for item in cart_items) + shipping_charges

        return JsonResponse({'quantity': cart.quantity, 'amount': amount, 'totalAmount': totalAmount})



# ==================================================Check_out==================================================================

def Checkout(request):
    if request.method == 'POST':
        totalamount = request.POST.get('totalamount')
        recipient_id = request.POST.get('recipient_id')
        # client = PayoneerClient(username=settings.PAYONEER_API_USERNAME,
        #                         password=settings.PAYONEER_API_PASSWORD,
        #                         partner_id=settings.PAYONEER_API_PARTNER_ID,
        #                         sandbox=settings.PAYONEER_API_SANDBOX_MODE)
    #    response = client.initiate_payment(recipient_id=recipient_id, totalamount=totalamount)
        # if response.get('status') == 'success':
        #     return JsonResponse({'status': 'success', 'payment_id': response['payment_id']})
        # else:
        #     return JsonResponse({'status': 'error', 'message': 'Failed to initiate payment'})
    return render(request, 'app/checkout.html')  

# @csrf_exempt
# def handle_payoneer_callback(request):
#     if request.method == 'POST':
#         payment_id = request.POST.get('payment_id')
#         status = request.POST.get('status')
#         if status == 'completed':
#             pass
#         elif status == 'cancelled':
#             pass
#         return JsonResponse({'status': 'success'})
#     return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
