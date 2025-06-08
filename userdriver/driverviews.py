from django.shortcuts import render,redirect,HttpResponse
from django.conf import settings
from django.core.mail import send_mail
import random
from packersmoversadmin.models import driver_registeration,driver_details,driver_account_details,booking_details,vehicle_choice,driverLocationUpdate
import datetime
import requests
from  django.http import JsonResponse
from django.shortcuts import render
from apiip import apiip
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import folium

# store basic information of driver and send verification otp to client
def driver_registration(request):

     if request.method == 'POST':
        d_otp=random.randint(1234532,9999999)
        d_otp_used=0
        d_created_at=datetime.datetime.now()
        d_full_names=request.POST['d_full_name']
        d_email=request.POST['d_email']
        d_passwd=request.POST['d_passwd']
        d_birth_date=request.POST['d_birth_date']
        d_address_pin=request.POST['d_address_pin']

        form=driver_registeration(d_full_name=d_full_names,d_email=d_email,d_passwd=d_passwd,d_birth_date=d_birth_date,d_otp=d_otp,d_otp_used=d_otp_used,d_created_at=d_created_at,d_login_status=0,d_address_pin=d_address_pin,driver_bnk_status=0,driver_details_status=0,d_activity_status=0,driver_approval_status=0)   
        
        form.save()
        subject = 'Verification OTP'
        message = f'Your OTP for email verification is: {d_otp}. Please use this OTP to verify your email.'
        from_email = settings.EMAIL_HOST_USER
        to_email = [d_email]
        send_mail(subject, message, from_email, to_email)
        return redirect("/driver/driver_otp_verify/")
     else:
        
        return render(request,'driverregisteration.html')

# verify driver using otp
def driver_otp_verify(request):
   if request.method == 'POST':
      d_email=request.POST['u_email']
      d_otp=request.POST['u_otp']
     
      verify_otp=driver_registeration.objects.filter(d_email=d_email,d_otp=d_otp)
      count_otp=verify_otp.count()
      if count_otp > 0 :
        verify_otp_update=driver_registeration.objects.filter(d_email=d_email,d_otp=d_otp).update(d_otp_used=1)

        
        return render(request,"driverlogin.html")
      else :
        fail_m="Retry!..."
        
        return render(request,"driverregisteration.html",{'message':fail_m})
   else:
      
      return render(request,'driververifyotp.html')

# authenticate driver using otp send in driver email
def driverlogin(request):
     if request.method == 'POST':
      u_email=request.POST['u_email']
      u_passwd=request.POST['u_passwd'] 
      u_login_date=datetime.datetime.now()
      u_login=driver_registeration.objects.filter(d_email=u_email,d_passwd=u_passwd)
      u_login_count=u_login.count()
      print("this is count .....",u_login_count)
      
      if u_login_count > 0:
        
            
         u_login_update=driver_registeration.objects.filter(d_email=u_email,d_passwd=u_passwd).update(d_login_status=1,d_login_at=u_login_date)
         for u_login in u_login: 

          request.session['d_id'] = u_login.d_id
         
         return redirect("/driver/driverdetails/")
      else :
       print("not login")
       return render(request,'driverlogin.html')
     else:
       print("not login in this")
       return render(request,'driverlogin.html')

# store the driver vehicle information    
def driverdetails(request):
   if request.session.get('d_id'):
      driver_id =request.session.get('d_id')
      driver_reg=driver_registeration.objects.get(d_id=driver_id)

      check_details=driver_details.objects.filter(d_id=driver_id)
      count_details=check_details.count()
      if count_details > 0:
         return redirect('/driver/driver_profile/')      
      else:
         if request.method == 'POST':
            d_vehicle_no=request.POST['d_vehicle_no']
            d_licence=request.FILES['d_licence']
            d_vehicle_r_c=request.FILES['d_vehicle_r_c']
            d_vehicle_accept=0
            d_vehicle_choice=request.POST['driver_vehicle_name']
            vehiclechoice_obj=vehicle_choice.objects.get(vehicle_ch_id=d_vehicle_choice)
            form=driver_details(d_id=driver_reg,d_vehicle_no=d_vehicle_no,d_licence=d_licence,d_vehicle_r_c=d_vehicle_r_c,d_vehicle_accept=d_vehicle_accept,driver_vehicle_id=vehiclechoice_obj)            
            form.save()         
            return redirect('/driver/driverbankdetails/')      
       
         else:
          vehiclechoice=vehicle_choice.objects.all()
          return render(request,'drivervehicledetailsform.html',{'vehiclechoice':vehiclechoice})
   else:
      return render(request,'driverlogin.html')

# store driver bank details
def driver_bank_details(request):
   if request.session.get('d_id'):
      driver_id=request.session.get('d_id')
      driver_reg=driver_registeration.objects.get(d_id=driver_id)
      
      print("driver is created session",driver_reg)
      check_details=driver_account_details.objects.filter(d_id=driver_id)
      count_details=check_details.count()
      if count_details > 0:
         return redirect('/driver/driverdetails/')      
      else:
         if request.method == 'POST':
            d_accnt_no=request.POST['d_accnt_no']
            d_acc_ifs=request.POST['d_acc_ifs']
            d_branch_name=request.POST['d_branch_name']
            d_bank_name=request.POST['d_bank_name']
            d_bank_accept=0
            d_image_doc=request.FILES['d_image_doc']
            form=driver_account_details(d_id=driver_reg,d_accnt_no=d_accnt_no,d_acc_ifs=d_acc_ifs,d_branch_name=d_branch_name,d_bank_name=d_bank_name,d_bank_accept=d_bank_accept,d_image_doc=d_image_doc)
            form.save()
            return redirect('/driver/driverbankdetails/')         
         else:
          return render(request,'driverbankdetailsform.html')
   else:
      return render(request,'driverlogin.html')

#display driver profile
def driver_profile(request):
   if request.session.get('d_id'):
     driver_id=request.session.get('d_id')
     driver_register=driver_registeration.objects.filter(d_id=driver_id)
     driver_vehicle=driver_details.objects.filter(d_id=driver_id)
     driver_account=driver_account_details.objects.filter(d_id=driver_id)
     return render(request,'viewprofile.html',{'driver_register':driver_register,'driver_vehicle':driver_vehicle,'driver_account':driver_account})
   else:
      return render(request,'driverlogin.html')

# display the driver bookings allocated by the admin 
def driver_booking(request):
   if request.session.get('d_id'):
      driver_id=request.session.get('d_id')
      driver_filter_activities=driver_registeration.objects.filter(d_id=driver_id)
      driver_book=booking_details.objects.filter(driver_all_id=driver_id)
      return render(request,'driverbooking.html',{'driver_book':driver_book,'driver_filter_activity':driver_filter_activities})
   else:
      return render(request,'driverlogin.html')

# update the driver status offline
def update_offline(request):
   if request.session.get('d_id'):
      driver_id=request.session.get('d_id')      
      driver_filter=driver_registeration.objects.filter(d_id=driver_id)
      driver_update_offline=driver_filter.update(d_activity_status=0)
      return redirect("/driver/driver_booking/")
   else:
      return render(request,'driverlogin.html')

# update the driver status offline      
def update_online(request):
   if request.session.get('d_id'):
      driver_id=request.session.get('d_id')
      driver_filter=driver_registeration.objects.filter(d_id=driver_id)
      driver_update_offline=driver_filter.update(d_activity_status=1)
      return redirect("/driver/driver_booking/")
   else:
      return render(request,'driverlogin.html')
# logout the driver
def driver_logout(request):
   del request.session['d_id']
   return render(request,'driverlogin.html')

@csrf_exempt
def driver_location(request):
    if request.method == "POST":
        # fetch the location longitude and longitude from frontend Ajax
        latitude = float(request.POST.get('latitude'))
        longitude = float(request.POST.get('longitude'))
        # Create a map centered at the coordinates
        mymap = folium.Map(location=[latitude, longitude], zoom_start=5)
        folium.Marker([latitude, longitude],popup=f"<b>Current Location</b><br>{latitude:.6f}, {longitude:.6f}",icon=folium.Icon(color='red', icon='info-sign')).add_to(mymap)
        figure.render()        
        return render(request, 'map.html', {'map': mymap})
    else:
        
        return render(request, 'map.html')


