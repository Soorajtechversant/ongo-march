from django.contrib import admin
from .models import HotelName, UserLoginDetails,UserLoginDetails,MerchantDetails
# Register your models here.

admin.site.register(HotelName)
admin.site.register(UserLoginDetails)
admin.site.register(MerchantDetails)

