from django import forms
from .models import user_registeration,driver_details,driver_account_details,booking_details,package_count,category_count,packages,category,vehicle_choice,driver_registeration



class categories(forms.ModelForm):
        
    class Meta:
        model = category
        fields = ['c_name','c_descr']

class package(forms.ModelForm):
    
    class Meta:
        model = packages
        fields =['pack_name' ,'pack_price','pack_descr','cat_id']

class new_vehicle(forms.ModelForm):
    
    class Meta:
        model = vehicle_choice 
        fields = ['vehicle_ch_name','vehicle_ch_height','vehicle_ch_width','vehicle_ch_length','vehicle_ch_km_price','vehicle_ch_capacity','vehicle_image','package_id']
 

    