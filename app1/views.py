
from django import views
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.shortcuts import render, HttpResponseRedirect
from .forms import RegisterForm, LoginForm, ChangePasswordForm, UserProfile
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.views import View
from .models import Customer, Cart, OrderPlaced, Product
from django.contrib import messages
from django.db.models import Q

# function based component ko lai Authenticate garney arko method
from django.contrib.auth.decorators import login_required
# class based ko lai
from django.utils.decorators import method_decorator


class HomeView(View):
    def get(self, request):
        mobile = Product.objects.filter(category='M')
        headphone = Product.objects.filter(category='HP')
        camera = Product.objects.filter(category='C')
        tshirt = Product.objects.filter(category='T')
        cartitem=0
        if request.user.is_authenticated:
            cartitem=len(Cart.objects.filter(user=request.user))

        return render(request, 'core/home.html', {'mobile': mobile, 'headphone': headphone, 'camera': camera, 'tshirt': tshirt,'cartitem':cartitem})


class product_detailView(View):
    def get(self, request, id):
        data = Product.objects.get(id=id)
        product_already_in_cart = False
        cartitem=0
        if request.user.is_authenticated:
            cartitem=len(Cart.objects.filter(user=request.user))
            product_already_in_cart = Cart.objects.filter(
                Q(product=data.id) & Q(user=request.user)).exists()
        return render(request, 'core/productdetail.html', {'data':data, 'product_already_in_cart': product_already_in_cart,'cartitem':cartitem})


class tshirtView(View):
    def get(self, request, data=None):

        if data == None:
            tshirt = Product.objects.filter(category='T')
        elif data == 'Nike' or data == 'Jordan' or data == 'Air':
            tshirt = Product.objects.filter(category='T').filter(brand=data)
        elif data == 'less':
            tshirt = Product.objects.filter(
                category='T').filter(discount_price__lte=100)
        elif data == 'between':
            tshirt = Product.objects.filter(category='T').filter(
                discount_price__gte=200).filter(discount_price__lte=1000)
        elif data == 'above':
            tshirt = Product.objects.filter(
                category='T').filter(discount_price__gte=200)
        cartitem=0
        if request.user.is_authenticated:
            cartitem=len(Cart.objects.filter(user=request.user))

        return render(request, 'core/tshirt.html', {'tshirt': tshirt,'cartitem':cartitem})


class add_to_cartView(View):
    def get(self, request,):
        user = request.user
        id = request.GET.get('prod_id')
        # print(id)
        # aba cart table ma addto cart gareko detail save garne
        product = Product.objects.get(id=id)
        obj = Cart(user=user, product=product)
        obj.save()
        return redirect('/showcart')

# 2 ta kina banako bhnda logic lekhna sajilo bhayera or mathi nai lekhda ni huntheo


class ShowcartView(View):
    def get(self, request):
        cartitem=0
        if request.user.is_authenticated:
            cartitem=len(Cart.objects.filter(user=request.user))

            user = request.user
            cart = Cart.objects.filter(user=user)
            amount = 0.0
            shipping_amount = 70.0
            total_amount = 0.0
            # list comprehension method
            cart_product = [p for p in Cart.objects.all() if p.user == user]
            # cart nahuna ni skxa so logic lekhne
            if cart_product:
                for p in cart_product:
                    tempamount = (p.quantity * p.product.seling_price)
                    amount = amount+tempamount
                    total_amount = amount + shipping_amount
            else:
                return redirect('/emptycart')

            return render(request, 'core/addtocart.html', {'carts': cart, 'amount': amount, 'total_amount': total_amount,'cartitem':cartitem})


class EmptyCardView(View):
    def get(self, request):
        cartitem=0
        if request.user.is_authenticated:
            cartitem=len(Cart.objects.filter(user=request.user))
        return render(request, 'core/emptycart.html',{'cartitem':cartitem})


class RemoveTtemCartView(View):
    def get(self, request, id):
        user = request.user
        # print(user)
        # print(id)
        cart = Cart.objects.filter(user=user).filter(product=id)
        cart.delete()
        return redirect('/showcart')


def plus_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        user = request.user
        cart = Cart.objects.get(Q(user=user) & Q(product=prod_id))
        cart.quantity += 1
        cart.save()
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        # list comprehension method
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.seling_price)
            amount = amount+tempamount
        data = {
            'quantity': cart.quantity,
            'amount': amount,
            'total_amount': amount + shipping_amount
        }
        return JsonResponse(data)


def minus_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        user = request.user
        cart = Cart.objects.get(Q(user=user) & Q(product=prod_id))
        cart.quantity -= 1
        cart.save()
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        # list comprehension method
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.seling_price)
            amount = amount+tempamount

        data = {
            'quantity': cart.quantity,
            'amount': amount,
            'total_amount': amount + shipping_amount
        }
        return JsonResponse(data)


def buy_now(request):

    return render(request, 'core/buynow.html')

           

def profile(request):
    cartitem=0
    if request.user.is_authenticated:
        cartitem=len(Cart.objects.filter(user=request.user))
        if request.method == "POST":
            form = UserProfile(request.POST)
            usr = request.user
            if form.is_valid():
                name = form.cleaned_data['name']
                city = form.cleaned_data['city']
                provience = form.cleaned_data['provience']
                post_code = form.cleaned_data['post_code']
                reg = Customer(user=usr, name=name, city=city,
                               provience=provience, post_code=post_code)
                reg.save()
                messages.success(request, 'Address Successfully added')
        form = UserProfile()
        return render(request, 'core/profile.html', {'form': form, 'active': 'btn-primary','cartitem':cartitem})
    else:
        return HttpResponseRedirect('/login/')


def address(request):
    cartitem=0
    if request.user.is_authenticated:
        cartitem=len(Cart.objects.filter(user=request.user))
    data = Customer.objects.all()
    return render(request, 'core/address.html', {'active': 'btn-primary', 'data': data,'cartitem':cartitem})

# @method_decorator(login_required,name='dispatch') class based ko lagi
# @login_required for function based


def orders(request):
    cartitem=0
    if request.user.is_authenticated:
        cartitem=len(Cart.objects.filter(user=request.user))
        OP = OrderPlaced.objects.filter(user=request.user)
        return render(request, 'core/orders.html', {'order_placed': OP,'cartitem':cartitem})
    return HttpResponseRedirect('/login/')


def change_password(request):
    cartitem=0
    if request.user.is_authenticated:
        cartitem=len(Cart.objects.filter(user=request.user))
        if request.method == "POST":
            form = ChangePasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return HttpResponseRedirect('/profile/')
        form = ChangePasswordForm(request.user)
        return render(request, 'core/changepassword.html', {'form': form,'cartitem':cartitem})
    return HttpResponseRedirect('/login/')


class mobileView(View):
    def get(self, request, data=None):
        cartitem=0
        if request.user.is_authenticated:
            cartitem=len(Cart.objects.filter(user=request.user))
        if data == None:
            mobile = Product.objects.filter(category='M')
        elif data == 'Apple' or data == 'Realme' or data == 'Samsung' or data == 'Oppo' or data == 'Huwai':
            mobile = Product.objects.filter(category='M').filter(brand=data)
        elif data == 'below':
            mobile = Product.objects.filter(
                category='M').filter(discount_price__lt=500)

        elif data == 'between':
            mobile = Product.objects.filter(category='M').filter(
                discount_price__gte=1000).filter(discount_price__lte=5000)

        elif data == 'above':
            mobile = Product.objects.filter(
                category='M').filter(discount_price__gt=5000)

        brands = Product.objects.filter(category='M')

        return render(request, 'core/mobile.html', {'brands': brands, 'mobile': mobile,'cartitem':cartitem})


def checkout(request):
    cartitem=0
    if request.user.is_authenticated:
        cartitem=len(Cart.objects.filter(user=request.user))
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 70.0
    total_amount = 0.0
    # list comprehension method
    cart_product = [p for p in Cart.objects.all() if p.user == user]
    # cart nahuna ni skxa so logic lekhne
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.seling_price)
            amount = amount+tempamount
            total_amount = amount + shipping_amount
    else:
        return redirect('/emptycart')
    return render(request, 'core/checkout.html', {'address': add, 'total_amount': total_amount, 'cart_items': cart_items,'cartitem':cartitem})


def PaymentDone(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OP = OrderPlaced(user=user, customer=customer,
                         product=c.product, quantity=c.quantity)
        OP.save()
        c.delete()
    return redirect("orders")


def customerregistration(request):
    if request.method == "POST":
        fm = RegisterForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Successfully Registered.')
    else:
        fm = RegisterForm()
    return render(request, 'core/customerregistration.html', {'form': fm})


def login_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                fname = fm.cleaned_data['username']
                ps = fm.cleaned_data['password']
                user = authenticate(username=fname, password=ps)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Successfully Login.')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = LoginForm()
        return render(request, 'core/login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login/')
