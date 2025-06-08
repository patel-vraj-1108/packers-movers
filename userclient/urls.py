from django.contrib import admin
from django.urls import path
from  . import clientviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path("clienttemplate/",clientviews.index_test),
    path("header_footer/",clientviews.header_footer),
    path("registeration/",clientviews.registration),
    path("otp_verify/",clientviews.otp_verify),
    path("login/",clientviews.login_user),
    path("category_data/",clientviews.category_data),
    path("packages_data/<int:id>",clientviews.packages_data),
    path("fetchkilometer/",clientviews.fetchperkilometer,name="fetchkilometer"),
    path("test_distances/",clientviews.test_distance,name="test_distances"),
    path("booking/<int:id>",clientviews.bookingdetails,name="booking"),
    ``   
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)