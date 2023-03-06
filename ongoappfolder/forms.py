from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms
from ongoappfolder.models import  HotelName


class HotelForm(forms.ModelForm):
    class Meta:
        model = HotelName
        fields = ('food','ingredients','stock','price','hotelimage','productpicture' ,)

    def save(self, request):
        
        owner = MerchantDetails.objects.get(
                    username__username=request.user.username)
        hotel = HotelName(food=self.cleaned_data['food'],ingredients=self.cleaned_data['ingredients'],price=self.cleaned_data['price'],hotelimage=self.cleaned_data['hotelimage'],productpicture=self.cleaned_data['productpicture'], stock=self.cleaned_data['stock'])
        hotel.owner = owner
        hotel.hotelname= owner.hotel_name
        
        hotel.save()
        return request

class CustomSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=255, required=True)
    phone = forms.CharField(max_length=14, required=True)
    address = forms.EmailField(max_length=255, required=True)
    class Meta:
        model = UserLoginDetails
        fields = ('username', 'email', 'phone' , 'address' ,  'password1', 'password2' )


class MerchantSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=255, required=True)
    hotelname = forms.CharField(max_length=255, required=True)
    phone = forms.CharField(max_length=12, required=True)
    businesstype = forms.CharField(max_length=255, required=True)
    address = forms.EmailField(max_length=255, required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'hotelname' , 'phone' , 'address' ,  'password1', 'password2' , 'businesstype')


