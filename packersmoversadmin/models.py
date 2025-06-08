from django.db import models

# store user and admin details
class user_registeration(models.Model):
    u_id=models.AutoField(primary_key=True) 
    u_full_name=models.TextField(max_length=70,null=False)
    u_email=models.EmailField(max_length=80,null=False)
    u_passwd=models.CharField(max_length=35,null=False)
    u_otp=models.IntegerField(null=False)
    u_otp_used=models.BooleanField(null=False)
    u_created_at=models.DateTimeField(null=False)
    u_login_at=models.DateTimeField(null=True,blank=True)
    u_login_status=models.IntegerField(null=False)
    u_birth_date=models.DateField(null=True)
    u_is_admin = models.IntegerField(null=False)


    def __str__(self):
        return self.u_full_name

    
    class Meta:
        db_table = 'user_registeration'
        managed = True
        verbose_name = 'user_registeration'
        verbose_name_plural = 'user_registeration'

#detail description of category such as category price range,types of package etc

class category(models.Model):
    c_id=models.AutoField(primary_key=True) 
    c_name=models.CharField(max_length=70,null=False)
    c_descr=models.TextField(max_length=70,null=False)
   


    def __str__(self):
        return self.c_name

    
    class Meta:
        db_table = 'category'
        managed = True
        verbose_name = 'category'
        verbose_name_plural = 'category'
# store category wise packages
# This table include types of material to be carried out,package price  etc

class packages(models.Model):
    pack_id=models.AutoField(primary_key=True) 
    pack_name=models.TextField(max_length=70,null=False)
    pack_price=models.IntegerField() 
    pack_descr=models.TextField(max_length=70,null=False)
    cat_id=models.ForeignKey(category,on_delete=models.CASCADE)


    def __str__(self):
        return self.pack_name
        return self.pack_price

    
    class Meta:
        db_table = 'packages'
        managed = True
        verbose_name = 'packages'
        verbose_name_plural = 'packages'

#store driver details
class driver_registeration(models.Model):
    d_id=models.AutoField(primary_key=True) 
    d_full_name=models.TextField(max_length=70,null=False)
    d_email=models.EmailField(max_length=80,null=False)
    d_passwd=models.CharField(max_length=35,null=False)
    d_otp=models.IntegerField(null=False)
    d_otp_used=models.BooleanField(null=False)
    d_created_at=models.DateTimeField(null=False)
    d_login_at=models.DateTimeField(null=True,blank=True)
    d_login_status=models.IntegerField(null=False)
    d_birth_date=models.DateField(null=True)
    d_activity_status=models.IntegerField(null=False)
    driver_details_status=models.IntegerField(null=False)
    driver_bnk_status=models.IntegerField(null=False)
    d_address_pin=models.IntegerField(null=False)
    driver_approval_status=models.IntegerField()


    

    
    class Meta:
        db_table = 'driver_registeration'
        managed = True
        verbose_name = 'driver_registeration'
        verbose_name_plural = 'driver_registeration'

class driverLocationUpdate(models.Model):
    d_id=models.ForeignKey(driver_registeration,on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    accuracy = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} at {self.timestamp}"


class vehicle_choice(models.Model):
    vehicle_ch_id=models.AutoField(primary_key=True) 
    vehicle_ch_name=models.TextField(max_length=70,null=False)
    vehicle_ch_height=models.IntegerField(null=False)
    vehicle_ch_width=models.IntegerField(null=False)
    vehicle_ch_length=models.IntegerField(null=False)
    vehicle_ch_km_price=models.IntegerField(null=False)
    vehicle_ch_capacity=models.IntegerField(null=False)
    vehicle_image=models.ImageField(upload_to="adminviehcle/")
    package_id=models.ForeignKey(packages,on_delete=models.CASCADE)



    def __str__(self):
        return self.vehicle_ch_name  
        return self.vehicle_ch_id         

    
    class Meta:
        db_table = 'vehicle_choice'
        managed = True
        verbose_name = 'vehicle_choice'
        verbose_name_plural = 'vehicle_choice'

#store drivers vehicle details like vehicle RC,driver licence in document format

class driver_details(models.Model):
    d_details_id=models.AutoField(primary_key=True) 
    d_id=models.ForeignKey(driver_registeration,on_delete=models.CASCADE)
    d_vehicle_no=models.TextField(max_length=40,null=False)
    d_licence=models.ImageField(upload_to="driverlicence/")
    d_vehicle_r_c=models.ImageField(upload_to="driverrc/")
    d_vehicle_accept=models.IntegerField(null=False)
    driver_vehicle_id=models.ForeignKey(vehicle_choice,on_delete=models.CASCADE)
    

    


    def __str__(self):
        return self.d_id
  
    class Meta:
        db_table = 'driver_details'
        managed = True
        verbose_name = 'driver_details'
        verbose_name_plural = 'driver_details'


#store drivers bank account details 

class driver_account_details(models.Model):
    d_acc_details_id=models.AutoField(primary_key=True,null=False) 
    d_id=models.ForeignKey(driver_registeration,on_delete=models.CASCADE)
    d_accnt_no=models.IntegerField(null=False)
    d_acc_ifs=models.TextField(max_length=90,null=False)
    d_branch_name=models.TextField(max_length=100,null=False)
    d_bank_name=models.TextField(max_length=100,null=False)
    d_bank_accept=models.IntegerField()
    d_image_doc=models.ImageField(upload_to="bankpassbook/")
    

    def __str__(self):
        return self.d_acc_details_id
  
    class Meta:
        db_table = 'driver_account_details'
        managed = True
        verbose_name = 'driver_account_details'
        verbose_name_plural = 'driver_account_details'










class category_count(models.Model):
    cat_count_id=models.AutoField(primary_key=True,null=False)
    cat_id=models.ForeignKey(category,on_delete=models.CASCADE)
    cat_count=models.IntegerField(null=False)

    def __str__(self):
        return self.cat_count_id
    class Meta:
        db_table = 'category_count'
        managed = True
        verbose_name = 'category_count'
        verbose_name_plural = 'category_count'

class package_count(models.Model):
    pack_count_id=models.AutoField(primary_key=True,null=False)
    pack_id=models.ForeignKey(category,on_delete=models.CASCADE)
    pack_count=models.IntegerField(null=False)

    def __str__(self):
        return self.cat_count_id
    
    class Meta:
        db_table = 'package_count'
        managed = True
        verbose_name = 'package_count'
        verbose_name_plural = 'package_count'

class booking_details(models.Model):
    booking_id=models.AutoField(primary_key=True,null=False)
    user_id=models.ForeignKey(user_registeration,on_delete=models.CASCADE)
    package_id=models.ForeignKey(packages,on_delete=models.CASCADE)
    from_address=models.TextField(null=False)
    from_pincode=models.IntegerField(null=False)
    from_contact=models.IntegerField(null=False)
    to_address=models.TextField(null=False)
    to_pincode=models.IntegerField(null=False)
    to_contact=models.IntegerField(null=False)
    vehicle_selection=models.ForeignKey(vehicle_choice,on_delete=models.CASCADE)
    driver_all_id=models.ForeignKey(driver_registeration,on_delete=models.CASCADE,null=True,blank=True)
    driver_all_STATUS=models.IntegerField(null=False)
    payment_status=models.IntegerField(null=False)
    total_pay_amount=models.IntegerField(null=False)
    driver_amount=models.IntegerField(null=False)
    portal_profit_amount=models.IntegerField(null=False)
    total_no_km_travel=models.IntegerField(null=False)
    booking_date=models.DateTimeField(null=False)
    booking_status=models.IntegerField(null=False)
    completion_otp=models.IntegerField(null=True) 

    def __str__(self):
        return self.booking_id
    
    class Meta:
        db_table = 'booking_details'
        managed = True
        verbose_name = 'booking_details'
        verbose_name_plural = 'booking_details'















