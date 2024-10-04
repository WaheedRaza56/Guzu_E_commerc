from django.contrib import admin
from django.urls import path,include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView, ShopView, BlogView,MyPasswordResetView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('shop', ShopView.as_view(), name='shop'),
    path('blog', BlogView.as_view(), name='blog'),
    path('contact', views.contact_view, name='contact'),
    path('checkOut/', views.Checkout, name='Checkout'),

    path('SignUp/', views.customerRegistrationView, name='SignUp'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('recovery/', MyPasswordResetView.as_view(), name='recovery'),  

    path('add-to-wishlist/',views.addtowishlist,name='addtowishlist'),
    path('delete-From-Wishlist/',views.deleteFromWishlist,name='deleteFromWishlist'),
    path('add-to-cart/',views.addtocart,name='addtocart'),
    path('delete-From-Cart/',views.deleteFromCart,name='deleteFromCart'),

    path('cart-price/',views.cart_price,name='cart_price'),
    path('plus-cart-price/',views.plus_cart_price,name='plus_cart_price'),
    path('minus-cart-price/',views.minus_cart_price,name='minus_cart_price'),
    # path('payoneer-callback/', views.handle_payoneer_callback, name='payoneer_callback'),


]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
