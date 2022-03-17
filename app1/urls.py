from re import template
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views 
from .forms import MyResetPasswordForm,MyResetNewPasswordForm

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('product-details/<int:id>/',
         views.product_detailView.as_view(), name='product-details'),
    path('cart/', views.add_to_cartView.as_view(), name='add_to_cart'),
    path('emptycart/', views.EmptyCardView.as_view(), name='emptycart'),
    path('showcart/',views.ShowcartView.as_view(), name='showcart'),
    path('removeitemcart/<int:id>/',views.RemoveTtemCartView.as_view(), name='removeitemcart'),
    path('pluscart/', views.plus_cart, name='plus_cart'),
    path('minuscart/', views.minus_cart, name='minus_cart'),
    path('buy/', views.buy_now, name='buy_now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobileView.as_view(), name='mobile'),
    path('tshirt/', views.tshirtView.as_view(), name='tshirt'),
    path('tshirt/<slug:data>/', views.tshirtView.as_view(), name='tshirtdata'),
    path('mobile/<slug:data>/', views.mobileView.as_view(), name='mobiledata'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.PaymentDone, name='paymentdone'),
     # authentication start
    path('registration/', views.customerregistration,
         name='customerregistration'),
    path('login/', views.login_user, name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='core/password_reset.html',
               form_class=MyResetPasswordForm),name="password_reset"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='core/password_reset_done.html'),
               name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='core/password_reset_confirm.html',
               form_class=MyResetNewPasswordForm),name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='core/password_reset_complete.html'),
               name="password_reset_complete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
