from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from  packersmoversadmin.models import user_registeration,driver_details,driver_account_details,booking_details,package_count,category_count,packages,category,vehicle_choice,driver_registeration
from packersmoversadmin.forms import user_registeration 
import datetime
import random
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import requests
# fetch category and display to index.html
def index_test(request):
    categorydata=category.objects.all()
    return render(request,"index.html",{'category':categorydata})
    
 # fetch category and display to headerfooter
def header_footer(request):
    categorydata=category.objects.all()
    return render(request,"headerfooter.html",{'category':categorydata})

# store the registeration information and send otp for verification
def registration(request):   
     if request.method == 'POST':
        u_otp=random.randint(1234532,9999999)
        u_otp_use=0
        u_created=datetime.datetime.now()
        u_full_nam=request.POST['u_full_name']
        u_email=request.POST['u_email']
        u_passw=request.POST['u_passwd']
        u_birth_date=request.POST['u_birth_date']
        form=user_registeration(u_full_name=u_full_nam,u_email=u_email,u_passwd=u_passw,u_is_admin=1,u_birth_date=u_birth_date,u_otp=u_otp,u_otp_used=u_otp_use,u_created_at=u_created,u_login_status=0)        
        form.save()
        subject = 'Verification OTP'
        message = f'Your OTP for email verification is: {u_otp}. Please use this OTP to verify your email.'
        from_email = settings.EMAIL_HOST_USER
        to_email = [u_email]
        send_mail(subject, message, from_email, to_email)
        return redirect("/client/otp_verify/")
     else:
        
        return render(request,'registeration.html')
    
# otp verification for the user
def otp_verify(request):
     if request.method == 'POST':
      u_email=request.POST['u_email']
      u_otp=request.POST['u_otp']
      u_otp_used=1
      u_is_admin=1
      verify_otp=user_registeration.objects.filter(u_email=u_email,u_otp=u_otp,u_is_admin=u_is_admin)
      count_otp=verify_otp.count()
      print("count number ...." , count_otp)
      if count_otp > 0 :
        verify_otp_update=user_registeration.objects.filter(u_email=u_email,u_otp=u_otp,u_is_admin=u_is_admin).update(u_otp_used=1)
        print("....................found ..........................")
        success_m="Registered successfully"
        return render(request,"login.html",{'message':success_m})
      else :
        fail_m="Retry!..."
        return render(request,"uotp.html",{'message':fail_m})
     else:
      
      return render(request,'uotp.html')
# Authanticate the user
def login_user(request):
         if request.method == 'POST':
          u_email=request.POST['u_email']
          u_passwd=request.POST['u_passwd'] 
          u_is_admin=1
          u_login_date=datetime.datetime.now()
          u_login=user_registeration.objects.filter(u_email=u_email,u_passwd=u_passwd,u_is_admin=u_is_admin)
          u_login_count=u_login.count()
          print(u_login_count)
          if u_login_count > 0:
           u_login_update=user_registeration.objects.filter(u_email=u_email,u_passwd=u_passwd,u_is_admin=u_is_admin).update(u_login_status=1,u_login_at=u_login_date)
           for u_login in u_login: 
            request.session['u_id'] = u_login.u_id
            print(request.session['u_id'])
            return redirect("/client/category_data/")
          else :
           print("not login")
           return render(request,'login.html')
         else:
           print("not login in this")
           return render(request,"login.html")

#fetch all category and display to the user in category.html
def category_data(request):
    categorydata=category.objects.all()
    print("................this is number of category",categorydata)
    return render(request,"category.html",{'category':categorydata})

#fetch all packages and display to the user in packages.html it will display after selecting category
def packages_data(request,id):
    packages_d=packages.objects.filter(cat_id=id)    
    return render(request,"packages.html",{'packages':packages_d})

# fetch per km price by selecting vehicle by the user
@csrf_exempt
def fetchperkilometer(request):
    if request.method == 'POST':
      print("......post request .....")
      vehicle_id=int(request.POST.get('vehicle_choice_id'))
      fetch_km=vehicle_choice.objects.filter(vehicle_ch_id=vehicle_id)
      fetch_km_list=list(fetch_km.values())
      print(".......fetch kilometer ..........",fetch_km_list) 
      return JsonResponse({'fetch_km_j':fetch_km_list})

# it will display the distance between two location from api gomap (third party api)
def test_distance(request):
    if request.method == 'POST':
        from_location=request.POST.get('from_address')
        to_location=request.POST.get('to_address')
        travel_modes="driving"
        api="AlzaSy3nzLRUifN_6ibD6wSRkYwHdfsXzVUOU1w"        
        url =f'https://maps.gomaps.pro/maps/api/distancematrix/json?avoid=%3Cstring%3E&destinations={to_location}&origins=  {from_location}&units=%3Cstring%3E&mode=%3Cstring%3E&key=AlzaSy3nzLRUifN_6ibD6wSRkYwHdfsXzVUOU1w'
        response=requests.get(url)
        distance_data=response.json()
        distance_in_meter=distance_data['rows'][0]['elements'][0]['distance']['value']
        integer_distance=int(distance_in_meter)/1000
        
        print("....your distance .. in ..meter",integer_distance)
        return JsonResponse({'distance_km':integer_distance})

# store booking details of the user 
def bookingdetails(request,id):
    if request.session.get('u_id'):        
        if request.method == 'POST':
            vehicle_required_id=request.POST['vehicle_required_id']
            f_address=request.POST['from_address']
            f_pincode=request.POST['from_pincode']
            f_contact=request.POST['from_contact']
            to_address=request.POST['to_address']
            to_pincode=request.POST['to_pincode']
            t_contact=request.POST['to_contact']
            total_no_km_travel=float(request.POST['total_no_km_travel'])*2
            fetchkm=float(request.POST['fetchkm'])
            ur_id=request.session.get('u_id')
            user_filter=user_registeration.objects.get(u_id=ur_id)
            package_instance=packages.objects.get(pack_id=id)
            vehicle_selection_instance=vehicle_choice.objects.get(vehicle_ch_id=vehicle_required_id)
            payment_status=0
            total_pay_amount= float(total_no_km_travel)*float(fetchkm)
            portal_profit_amount = float(float(total_no_km_travel)*float(fetchkm)*0.10)
            driver_amount=float(float(total_pay_amount)-float(portal_profit_amount))
            book_dates=datetime.datetime.now()
            booking_status=0
            package_details_fetch=packages.objects.filter(pack_id=id)
            booking_store=booking_details(user_id=user_filter,from_address=f_address,from_pincode=f_pincode,from_contact=f_contact,to_address=to_address,to_pincode=to_pincode,to_contact=t_contact,total_no_km_travel=total_no_km_travel,payment_status=payment_status,total_pay_amount=total_pay_amount,portal_profit_amount=portal_profit_amount,driver_amount=driver_amount,booking_date=book_dates,booking_status=booking_status,package_id=package_instance,vehicle_selection=vehicle_selection_instance,driver_all_STATUS=0)
            booking_store.save()
            booking_details_id_instance=booking_details.objects.get(booking_date=book_dates,user_id=user_filter)
            booking_details_id=booking_details_id_instance.booking_id
            total_pay_amount= int(total_no_km_travel)*int(fetchkm)
            return render(request,"checkout.html",{'f_address':f_address,'f_contact':f_contact,'to_address':to_address,'to_pincode':to_pincode,'t_contact':t_contact,'total_no_km_travel':total_no_km_travel,'fetchkm':fetchkm,'user_filter':ur_id,'vehicle_selection_instance':vehicle_selection_instance,'total_pay_amount':total_pay_amount,'package_details_fetch':package_details_fetch,'booking_details_id':booking_details_id})
        else:
            vehicle_ch=vehicle_choice.objects.filter(package_id=id)
            return render(request,"clientbookingdetails.html",{'choose_vehicle':vehicle_ch,'id':id})
    else:
        return redirect('/client/login_user/')

def checkout(request):
    return render(request,"checkout.html")

# razorpay payment api
def payamount(request,id):
    if request.session.get('u_id'):
        if request.method == 'POST':
          booking_detail_instance=booking_details.objects.get(booking_id=id)
          return render(request,'payment_choice.html',{'booking_detail_instance':booking_detail_instance} )

# display booking details
def bookinghistory(request):
    return render(request,"bookinghistory.html")        
  

    
