from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import user_registeration,driver_details,driver_account_details,booking_details,package_count,category_count,packages,category,vehicle_choice,driver_registeration
from .forms import categories,package,new_vehicle
import datetime
import random
from django.core.mail import send_mail
from django.conf import settings
from django.core.exceptions import FieldDoesNotExist,SuspiciousOperation,ViewDoesNotExist

# header footer
def header_footer(request):
    return render(request,"header_footer.html")

# display users details
def usermaster(request):
    if request.session.get('u_id'):
      print(request.session.get('u_id'))
      userdata=user_registeration.objects.all()
      return render(request,'userdetails.html',{'userdetails':userdata})
    else:
      print("not login")
      return redirect("/moversadmin/adminlogin/")
       
# display unverified drivers
def drivermaster(request):
    if request.session.get('u_id'):
        driverdata=driver_registeration.objects.filter(driver_details_status=0,driver_bnk_status=0)
        return render(request,'driversdetails.html',{'drivermaster':driverdata})
    else:
      print("not login")
      return redirect("/moversadmin/adminlogin/")

#display verified driver
def authorized_driver(request):
    if request.session.get('u_id'):
            authorized_driver_data=driver_registeration.objects.filter(driver_details_status=1,driver_bnk_status=1)
            return render(request,'authorized_driver.html',{'authorize_driver':authorized_driver_data})
    else:
      print("not login")
      return redirect("/moversadmin/adminlogin/")

#display driver details
def driver_vehicle_details(request,id):
    if request.session.get('u_id'):
        driver_v_data=driver_details.objects.filter(d_id=id)
        return render(request,'drivervehicledetails.html',{'driver_vehicle_details':driver_v_data})
    else:
      print("not login")
      return redirect("/moversadmin/adminlogin/")

# display driver bank details
def driver_bnk_account(request,id):
    if request.session.get('u_id'):
        driver_bnk_data=driver_account_details.objects.filter(d_id=id)
        return render(request,'driveraccountdetail.html',{'driver_bnk_account':driver_bnk_data})
    else:
      print("not login")
      return redirect("/moversadmin/adminlogin/")
# display category details
def categorydetails(request):
    if request.session.get('u_id'):
        categorydata=category.objects.all()
        return render(request,'categorydetails.html',{'categorydetails':categorydata})
    else:
      print("not login")
      return redirect("/moversadmin/adminlogin/")
# display package details
def package_details(request):
    if request.session.get('u_id'):
        package_data=packages.objects.all()
        return render(request,'packagedetails.html',{'package_details':package_data})
    else:
      print("not login")
      return redirect("/moversadmin/adminlogin/")

# display the type vehicles are provided to the user
def vehicle_available(request):
    if request.session.get('u_id'):
        vehicle_avial=vehicle_choice.objects.all()
        return render(request,'vehicleavailable.html',{'vehicle_available':vehicle_avial})
    else:
      print("not login")
      return redirect("/moversadmin/adminlogin/")
# display the booking details of usewr like location, total kilometer  
def bookingdetails(request):
    if request.session.get('u_id'):
        bookingdata=booking_details.objects.filter(driver_all_STATUS=0)
        return render(request,'bookingdetails.html',{'bookingdetails':bookingdata})
    else:
      print("not login")
      return redirect("/moversadmin/adminlogin/")

# this function is used to delete user account from admin side
def usermaster_delete(request,id):
    if request.session.get('u_id'):
        userdata=user_registeration.objects.all()
        userdata_delete=user_registeration.objects.filter(u_id=id)
        userdata_delete.delete()
        return render(request,'userdetails.html',{'userdetails':userdata})
    else:
      print("not login")
      return redirect("/moversadmin/adminlogin/")


# this function is used to delete driver account from admin side
def drivermaster_delete(request,id):
     if request.session.get('u_id'):
        driverdata=driver_registeration.objects.all()
        driverdata_delete=driver_registeration.objects.filter(d_id=id)
        driverdata_delete.delete()
        return render(request,'driversdetails.html',{'drivermaster':driverdata})
     else:
      print("not login")
      return redirect("/moversadmin/adminlogin/")

# this function is used to delete drivers vehicle details from admin side
def driver_vehicle_details_delete(request,id):
    if request.session.get('u_id'):
        driver_v_data=driver_details.objects.all()
        driver_v_data_delete=driver_details.objects.filter(d_details_id=id)
        driver_v_data_delete.delete()
        return render(request,'drivervehicledetails.html',{'driver_vehicle_details':driver_v_data})
    else:
      print("not login")
      return redirect("/moversadmin/adminlogin/")

# this function is used to delete driver bank account from admin side
def driver_bnk_account_delete(request,id):
    if request.session.get('u_id'):
            driver_bnk_data=driver_account_details.objects.all()
            driver_bnk_data_delete=driver_account_details.objects.filter(d_acc_details_id=id)
            driver_bnk_data_delete.delete()
            return render(request,'driveraccountdetail.html',{'driver_bnk_account':driver_bnk_data})
    else:
      print("not login")
      return redirect("/moversadmin/adminlogin/")

# update the driver verification to verified or not verified driver
def update_driver_verification(request,id):
    if request.session.get('u_id'):
        driver_verify_filter=driver_registeration.objects.filter(d_id=id)
        driver_verification=driver_verify_filter.update(driver_details_status=1,driver_bnk_status=1)
        return redirect("/moversadmin/drivermaster/")
    else:
      print("not login")
      return redirect("/moversadmin/adminlogin/")


#  delete categories by admin 
def categorydetails_delete(request,id):
    if request.session.get('u_id'):
        categorydata=category.objects.all()
        categorydata_delete=category.objects.filter(c_id=id)
        categorydata_delete.delete()
        return render(request,'categorydetails.html',{'categorydetails':categorydata})
    else:
      print("not login")
      return redirect("/moversadmin/adminlogin/")


# delete packages by admin 
def package_details_delete(request,id):
    if request.session.get('u_id'):
        package_data=packages.objects.all()
        package_data_delete=packages.objects.filter(pack_id=id)
        package_data_delete.delete()
        return render(request,'packagedetails.html',{'package_details':package_data})
    else:
      print("not login")
      return redirect("/moversadmin/adminlogin/")

# delete vehicle provided by admin 

def vehicle_available_delete(request,id):
    if request.session.get('u_id'):
        vehicle_avial=vehicle_choice.objects.all()
        vehicle_avial_delete=vehicle_choice.objects.filter(vehicle_ch_id=id)
        vehicle_avial_delete.delete()
        return render(request,'vehicleavailable.html',{'vehicle_available':vehicle_avial})
    else:
      print("not login")
      return redirect("/moversadmin/adminlogin/")

# this function is used to delete booking from admin side
def bookingdetails_delete(request,id):
    if request.session.get('u_id'):
        bookingdata=booking_details.objects.all()
        bookingdata_delete=booking_details.objects.filter(booking_id=id)
        bookingdata_delete.delete()
        return render(request,'bookingdetails.html',{'bookingdetails':bookingdata})
    else:
      print("not login")
      return redirect("/moversadmin/adminlogin/")


#add new categories
def add_new_category(request):
    if request.session.get('u_id'):
        try:
            categorydata=category.objects.all()
            if request.method == 'POST':
                form=categories(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect("/moversadmin/categorydetails/")
            else:
                categoryform=categories()
                return render(request,'categoryform.html',{'form':categoryform})
        # these exception is occurs when the database field is not matches with the given user data in form
        except FieldDoesNotExist :
            now = datetime.datetime.now()
            message="field doesn't matches" % now
            categoryform=categories()
            return render(request,'categoryform.html',{'form':categoryform,'message':message})
        # these exception is occurs when the suspicious activities are performed by the user
        except SuspiciousOperation :
            now = datetime.datetime.now()
            message="YOU ARE CAUGHT WITH SUSPICIOUS ACTIVITIES" % now
            categoryform=categories()
            return render(request,'categoryform.html',{'form':categoryform,'message':message})
        # These exception is occurs when their is problem in setting or configuration
        except ViewDoesNotExist :
            now = datetime.datetime.now()
            message="SORRY FOR INTERRUPTION CAN YOU PLEASE TRY AGAIN LATER DUE TO INVALID URL CONFIGURATION" % now
            categoryform=categories()
            return render(request,'categoryform.html',{'form':categoryform,'message':message})
        #these exception is occurs when there no middleware is working
        except MiddlewareNotUsed :
            now = datetime.datetime.now()
            message="SORRY FOR INTERRUPTION CAN YOU PLEASE TRY AGAIN LATER DUE TO INVALID  CONFIGURATION" % now
            categoryform=categories()
            return render(request,'categoryform.html',{'form':categoryform,'message':message})
        # for other exception else block will execute
        else:
            now = datetime.datetime.now()
            message="SORRY try again later" % now
            categoryform=categories()
            return render(request,'categoryform.html',{'form':categoryform,'message':message})
    else:
      print("not login")
      return redirect("/moversadmin/adminlogin/")



# ADD NEW PACKAGES
def add_new_packages(request):
    if request.session.get('u_id'):
        try:
            categorydata=category.objects.all()
            if request.method == 'POST':
                form=package(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect("/moversadmin/package_details/")
            else:
                packageform=package()
                return render(request,'addpackages.html',{'form':packageform,'categorydata':categorydata})
        # these exception is occurs when the database field is not matches with the given user data in form
        except FieldDoesNotExist :
            now = datetime.datetime.now()
            message="field doesn't matches" % now
            packageform=package()
            return render(request,'addpackages.html',{'form':packageform,'message':message})
        # these exception is occurs when the suspicious activities are performed by the user
        except SuspiciousOperation :
            now = datetime.datetime.now()
            message="YOU ARE CAUGHT WITH SUSPICIOUS ACTIVITIES" % now
            packageform=package()
            return render(request,'addpackages.html',{'form':packageform,'message':message})
        # These exception is occurs when their is problem in setting or configuration
        except ViewDoesNotExist :
            now = datetime.datetime.now()
            message="SORRY FOR INTERRUPTION CAN YOU PLEASE TRY AGAIN LATER DUE TO INVALID URL CONFIGURATION" % now
            packageform=package()
            return render(request,'addpackages.html',{'form':packageform,'message':message})
        #these exception is occurs when there no middleware is working
        except MiddlewareNotUsed :
            now = datetime.datetime.now()
            message="SORRY FOR INTERRUPTION CAN YOU PLEASE TRY AGAIN LATER DUE TO INVALID  CONFIGURATION" % now
            packageform=package()
            return render(request,'addpackages.html',{'form':packageform,'message':message})
        # for other exception else block will execute
        else:
            now = datetime.datetime.now()
            message="SORRY try again later" % now
            packageform=package()
            return render(request,'addpackages.html',{'form':packageform,'message':message})
    else:
      print("not login")
      return redirect("/moversadmin/adminlogin/")
  



# Add new viehcles
def add_new_viehcle(request):
    if request.session.get('u_id'):
        if request.method == 'POST':
            form=new_vehicle(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect("/moversadmin/vehicle_available/")
        else:
            form=new_vehicle()
            return render(request,'addviehcle.html',{'form':form})
    else:
      print("not login")
      return redirect("/moversadmin/adminlogin/")
 
# Add new admin
def addadmin(request):
    if request.session.get('u_id'):
        if request.method == 'POST':
            u_otp=random.randint(1234532,9999999)
            u_otp_use=0
            u_created=datetime.datetime.now()
            u_full_nam=request.POST['u_full_name']
            u_email=request.POST['u_email']
            u_passw=request.POST['u_passwd']
            u_birth_date=request.POST['u_birth_date']
            form=user_registeration(u_full_name=u_full_nam,u_email=u_email,u_passwd=u_passw,u_is_admin=0,u_birth_date=u_birth_date,u_otp=u_otp,u_otp_used=u_otp_use,u_created_at=u_created,u_login_status=0)           
            form.save()
            subject = 'Verification OTP'
            message = f'Your OTP for email verification is: {u_otp}. Please use this OTP to verify your email.'
            from_email = settings.EMAIL_HOST_USER
            to_email = [u_email]
            send_mail(subject, message, from_email, to_email)
            return redirect("/moversadmin/otp_verify/")
        else:        
            return render(request,'addadminform.html')
    else:
      print("not login")
      return redirect("/moversadmin/adminlogin/")
 
# verify Admin email
def otp_verify(request):
    if request.session.get('u_id'):
        if request.method == 'POST':
                u_email=request.POST['u_email']
                u_otp=request.POST['u_otp']
                u_otp_used=1
                verify_otp=user_registeration.objects.filter(u_email=u_email,u_otp=u_otp)
                count_otp=verify_otp.count()
                if count_otp > 1 :
                    verify_otp_update=user_registeration.objects.filter(u_email=u_email,u_otp=u_otp).update(u_otp_used=1)

                    success_m="Registered successfully"
                    return render(request,"addadminform.html",{'message':success_m})
                else :
                    fail_m="Retry!..."
                    return render(request,"addadminform.html",{'message':fail_m})
        else:           
            return render(request,'verifyotp.html')
    else:
      print("not login")
      return redirect("/moversadmin/adminlogin/")

# authenticate admin   
def adminlogin(request):
     if request.method == 'POST':
            u_email=request.POST['u_email']
            u_passwd=request.POST['u_passwd'] 
            u_login_date=datetime.datetime.now()
            u_login=user_registeration.objects.filter(u_email=u_email,u_passwd=u_passwd)
            u_login_count=u_login.count()
            
            if u_login_count > 0:
                u_login_update=user_registeration.objects.filter(u_email=u_email,u_passwd=u_passwd).update(u_login_status=1,u_login_at=u_login_date)
                for u_login in u_login: 

                    request.session['u_id'] = u_login.u_id
                    return redirect("/moversadmin/userdata/")
            else :
                return render(request,'adminlogin.html')
       
     else:
      
       return render(request,'adminlogin.html')



# update driver categories
def update_categories(request,id):
   
    if request.session.get('u_id'):
        
        if request.method == 'POST':
            update_c_name=request.POST['c_name']
            update_c_descr=request.POST['c_descr']
            update_category=category.objects.filter(c_id=id).update(c_name=update_c_name,c_descr=update_c_descr)
            fetch_category=category.objects.filter(c_id=id)
            return render(request,'updatecategoryform.html',{'fetch_category':fetch_category,'id':id})
        else:
            fetch_category=category.objects.filter(c_id=id)
            return render(request,'updatecategoryform.html',{'fetch_category':fetch_category,'id':id})
    else:
        return render(request,'adminlogin.html')
# update driver package
def update_packages(request,id):
    if request.session.get('u_id'):
        fetch_packages=packages.objects.filter(pack_id=id)
        if request.method == "POST":
            pack_name=request.POST['pack_name']
            pack_price=request.POST['pack_price']
            pack_descr=request.POST['pack_descr']
            cat_id=request.POST['cat_id']
            update_packages=packages.objects.filter(pack_id=id).update(pack_name=pack_name,pack_price=pack_price,pack_descr=pack_descr,cat_id=cat_id)
            return render(request,"updatepackages.html",{'fetch_packages':fetch_packages,'id':id})
        else:
            fetch_cat=category.objects.all()
            return render(request,"updatepackages.html",{'fetch_packages':fetch_packages,'id':id,'fetch_category':fetch_cat}) 
    else:
      return render(request,'adminlogin.html')  


# driver allocation for the bookings
def driverallocation(request,id):
    if request.session.get('u_id'):
        if request.method == 'POST':
            driver_id = request.POST['d_id']
            driver_id_instance=driver_registeration.objects.get(d_id=driver_id)         
            bookings_id = booking_details.objects.filter(booking_id=id) 
            booking_update=bookings_id.update(driver_all_id=driver_id_instance,driver_all_STATUS=1)
            return redirect("/moversadmin/bookingdetails/")
        else:
            drivers_details=driver_details.objects.all()
            bookings_id = booking_details.objects.filter(booking_id=id)
            for data in bookings_id:
                book_id = data.booking_id
            return render(request,"driverallocation.html",{'driverdetals':drivers_details,'bookings_details_id':book_id})
    else:
      return render(request,'adminlogin.html')  

# logout Admin
def logout(request):
   print(request.session.get('u_id'))
   id = request.session.get('u_id')
   del id
   return redirect('/moversadmin/adminlogin/')
            






    





       


      
   
