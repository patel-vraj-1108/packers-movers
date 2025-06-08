from django.contrib import admin
from django.urls import path,include
from . import driverviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('driverRegisteration/',driverviews.driver_registration,name='driverRegisteration'),
  path('driver_otp_verify/',driverviews.driver_otp_verify,name='driver_otp_verify'),
  path('driverlogin/',driverviews.driverlogin,name='driverlogin'),
  path('driverdetails/',driverviews.driverdetails,name='driver_details'),
  path('driverbankdetails/',driverviews.driver_bank_details,name='driver_bank_details'),
  path('driver_profile/',driverviews.driver_profile,name='driver_profile'),
  path('driver_booking/',driverviews.driver_booking,name='driver_booking'),
  path('update_online/',driverviews.update_online,name='update_online'),
  path('update_offline/',driverviews.update_offline,name='update_offline'),
  path('driver_logout/',driverviews.driver_logout,name='driver_logout'),
  path('driver_location/', driverviews.driver_location, name='driver_location'),
  # path('driver_get_location/', driverviews.driver_get_location, name='driver_get_location'),


  









 

  


]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
