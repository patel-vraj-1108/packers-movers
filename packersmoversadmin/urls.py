from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import adminviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('headerfooter/',adminviews.header_footer),
    path('userdata/',adminviews.usermaster),
    path('drivermaster/',adminviews.drivermaster),
    path('driver_vehicle_details/<int:id>',adminviews.driver_vehicle_details),
    path('driver_bnk_account/<int:id>',adminviews.driver_bnk_account),
    path('categorydetails/',adminviews.categorydetails),
    path('package_details/',adminviews.package_details),
    path('vehicle_available/',adminviews.vehicle_available),
    path('bookingdetails/',adminviews.bookingdetails),
    path('authorized_driver/',adminviews.authorized_driver),

    #delete urls
    path('userdata_delete/<int:id>',adminviews.usermaster_delete),
    path('drivermaster_delete/<int:id>',adminviews.drivermaster_delete),
    path('driver_vehicle_details_delete/<int:id>',adminviews.driver_vehicle_details_delete),
    path('driver_bnk_account_delete/<int:id>',adminviews.driver_bnk_account_delete),
    path('categorydetails_delete/<int:id>',adminviews.categorydetails_delete),
    path('package_details_delete/<int:id>',adminviews.package_details_delete),
    path('vehicle_available_delete/<int:id>',adminviews.vehicle_available_delete),
    path('bookingdetails_delete/<int:id>',adminviews.bookingdetails_delete),
    #redirect to form which adds categories
    path('add_categories/',adminviews.add_new_category),
    path('add_packages/',adminviews.add_new_packages),
    path('add_vehicle/',adminviews.add_new_viehcle),
    path('addadmin/',adminviews.addadmin,name="addadmin"),
    path('otp_verify/',adminviews.otp_verify),
    path('adminlogin/',adminviews.adminlogin,name="adminlogin"),
    path('adminlogout/',adminviews.logout,name="adminlogin"),

    #urls for updating  update_packages
    path('update_categories/<int:id>',adminviews.update_categories,name="update_categories"),
    path('update_packages/<int:id>',adminviews.update_packages,name="update_categories"),
    path('update_driver_verification/<int:id>',adminviews.update_driver_verification,name="update_driver_verification"),
    path('driverallocation/<int:id>',adminviews.driverallocation,name="driverallocation"),

    








    

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

