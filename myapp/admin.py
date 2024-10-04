from django.contrib import admin
from .models import *


@admin.register(slider1)
class slider1Admin(admin.ModelAdmin):
    list_display = ['id','para1','heading','para2','bg_img']

@admin.register(slider2)
class slider2Admin(admin.ModelAdmin):
    list_display = ['id','para1','bg_img']

@admin.register(handPicked_product)
class handPickedProductAdmin(admin.ModelAdmin):
    list_display = ['id','para1','heading','bg_img','hover_img']

@admin.register(banner)
class bannerAdmin(admin.ModelAdmin):
    list_display = ['id','heading','bg_img']

@admin.register(services)
class servicesAdmin(admin.ModelAdmin):
    list_display = ['id','heading','para1','bg_img']

@admin.register(Blog)
class blogAdmin(admin.ModelAdmin):
    list_display = ['id','para1','fashion','heading','para2','bg_img']


@admin.register(instaPic)
class instaPicAdmin(admin.ModelAdmin):
    list_display = ['id','bg_img']


@admin.register(discount_offer)
class discount_offerAdmin(admin.ModelAdmin):
    list_display = ['id','para1','heading','link']

# main end 

@admin.register(footer)
class footerAdmin(admin.ModelAdmin):
    list_display = ['id','para1','heading','link','para2','para3']

@admin.register(column1)
class column1Admin(admin.ModelAdmin):
    list_display = ['id','link1','heading','link2','link3','link4']

@admin.register(column2)
class column2Admin(admin.ModelAdmin):
    list_display = ['id','link1','heading','link2','link3','link4']

@admin.register(column3)
class column3Admin(admin.ModelAdmin):
    list_display = ['id','link1','heading','link2','link3','link4']

@admin.register(colunm4)
class column4Admin(admin.ModelAdmin):
    list_display = ['id','link1','heading','link2','link3','link4']


    # footer end 


@admin.register(shop_offer)
class shop_offerAdmin(admin.ModelAdmin):
    list_display = ['id','dropButton','heading','dropdown1','dropdown2','dropdown3']

@admin.register(filter_product)
class handPickedProductAdmin(admin.ModelAdmin):
    list_display = ['id','para1','heading','bg_img','hover_img']


# shop end 

@admin.register(blogList)
class blogListAdmin(admin.ModelAdmin):
    list_display = ['id','para1','heading','para2','bg_img','link']

@admin.register(catogery)
class catogeryAdmin(admin.ModelAdmin):
    list_display = ['id','link1','heading','link2','link3','link4']

@admin.register(Latest_Post)
class Latest_PostAdmin(admin.ModelAdmin):
    list_display = ['id','heading','para1','bg_img']

@admin.register(Tags)
class catogeryAdmin(admin.ModelAdmin):
    list_display = ['id','link1','heading','link2','link3','link4','bg_img']

# blog end 

@admin.register(contact_heading)
class contact_headingAdmin(admin.ModelAdmin):
    list_display = ['id','heading','para1','heading2','heading3']

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['id','heading1','heading2','heading3','para1','para2','para3','para4','para5','link']

@admin.register(Customer)
class CustomerAddressAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','phoneNo','website','content']

@admin.register(GetIntoTech)
class GetIntoTechAdmin(admin.ModelAdmin):
    list_display = ['id','heading','para1']


# cart folder


@admin.register(cartheading)
class cartheadingAdmin(admin.ModelAdmin):
    list_display = ['id','heading','para1','para2','para3']

@admin.register(ifEmpty)
class ifEmptyAdmin(admin.ModelAdmin):
    list_display = ['id','link','para1','bg_img']

@admin.register(items)
class itemsAdmin(admin.ModelAdmin):
    list_display = ['id','link','para1','para2','para3','para4','para5','bg_img']

@admin.register(box)
class itemsModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','items','quantity']

@admin.register(OptionCart)
class OptionCartAdmin(admin.ModelAdmin):
    list_display = ['id','para1','para2','bg_img','hover_img']

@admin.register(warning)
class warningAdmin(admin.ModelAdmin):
    list_display = ['id','para']

@admin.register(footercart)
class footercartAdmin(admin.ModelAdmin):
    list_display = ['id','para1','para2']

# wishlist folder

@admin.register(wishlistheading)
class cartheadingAdmin(admin.ModelAdmin):
    list_display = ['id','heading']

@admin.register(Wishlist)
class wishlistAdmin(admin.ModelAdmin):
    list_display = ['id','link','para1','para2','para3','para4','para5','bg_img']


@admin.register(Optionwishlist)
class OptionwishlistAdmin(admin.ModelAdmin):
    list_display = ['id','para1','para2','bg_img','hover_img']

@admin.register(EmptyWishlist)
class EmptyWishlistAdmin(admin.ModelAdmin):
    list_display = ['id','link','para1','bg_img']



# search folder 


@admin.register(search)
class searchAdmin(admin.ModelAdmin):
    list_display = ['id','heading','dropdown1','dropdown2','dropdown3']

@admin.register(QuickSearch)
class QuickSearchAdmin(admin.ModelAdmin):
    list_display = ['id','para','link1','link2','link3']

@admin.register(OptionSearch)
class OptionSearchAdmin(admin.ModelAdmin):
    list_display = ['id','para1','para2','bg_img','hover_img']


# account form 

@admin.register(account)
class accountAdmin(admin.ModelAdmin):
    list_display = ['id','heading1','heading2']

@admin.register(wishlists)
class wishlistsAdmin(admin.ModelAdmin):
    list_display = ['id','user','productes','Date','quantity']

@admin.register(User_Cart)
class User_CartAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']

@admin.register(CheckoutAddress)
class CheckoutAddressAdmin(admin.ModelAdmin):
    list_display = ['id','user','fname','lname','email','region','address','apartment','town','postcode','country','phoneNo','OrderNote']

@admin.register(order)
class orderAdmin(admin.ModelAdmin):
    list_display = ['id','user','total_amount','payment_method']

@admin.register(orderItem)
class orderItemAdmin(admin.ModelAdmin):
    list_display = ['order_no','product','quantity']