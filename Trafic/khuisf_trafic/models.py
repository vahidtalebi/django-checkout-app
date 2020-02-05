from django.db import models
class Users(models.Model):
    firstname=models.CharField(max_length=70)
    lastname=models.CharField(max_length=70)
    fathername=models.CharField(max_length=50)
    time_of_birth=models.DateTimeField()
    national_code=models.IntegerField()
    mobile_number=models.IntegerField()
    gender=models.BooleanField()#تغییر کرده
    personal_pic=models.ImageField( upload_to='user_image', height_field=None, width_field=None, max_length=None)#؟
    marital_status=models.CharField(max_length=70)
    std_code=models.IntegerField()
    majar=models.CharField(max_length= 120)
    enter_yaer=models.IntegerField()
    field=models.CharField(max_length=120)
    gerayesh=models.CharField(max_length=120)
    address=models.CharField(max_length=1200)
    phone_number=models.IntegerField()
    zip_code=models.IntegerField()
    finger_print=models.CharField(max_length=1200)#?
    otp=models.IntegerField()
    state=models.CharField(max_length=120)
    driving_licence_number=models.IntegerField()
    driving_licence_years=models.IntegerField()
    driving_licence_date=models.DateTimeField()
    driving_licence_fr_photo=models.CharField( max_length=1200)
    driving_licence_ba_photo=models.CharField( max_length=1200)
    def __str__(self):
        return self.firstname+" "+self.lastname
    
class Gates(models.Model):
    name=models.CharField( max_length=50)

class Enter_cars(models.Model):
    user_id=models.ForeignKey(Users, on_delete=models.CASCADE)
    date=models.DateTimeField( auto_now=False, auto_now_add=False)
    enter_time=models.DateTimeField( auto_now=False, auto_now_add=True)
    exit_time=models.DateTimeField( auto_now=False, auto_now_add=False)
    gates_id=models.ForeignKey(Gates, on_delete=models.CASCADE)
    car_tag=models.CharField( max_length=50)
    car_photo=models.CharField( max_length=1200)
    car_color=models.CharField( max_length=50)
    car_type=models.CharField( max_length=50)


    def __str__(self):
        return self.user_id

class Access_type(models.Model):
    type=models.CharField( max_length=50)
    def __str__(self):
        return self.type
    
class Admins(models.Model):
    fristname=models.CharField( max_length=70)
    lastname=models.CharField( max_length=70)
    national_code=models.IntegerField()
    personnel_code=models.IntegerField()
    fathername=models.CharField( max_length=70)
    mobile_number=models.IntegerField()
    gender=models.BooleanField()#! change this
    personnel_image=models.ImageField( upload_to='admin_image', height_field=None, width_field=None, max_length=None)#?!
    access_type_id=models.OneToOneField(Access_type, on_delete=models.CASCADE)
    def __str__(self):
        return self.personnel_code
class Logs(models.Model):
    admin_id=models.ForeignKey(Admins, on_delete=models.CASCADE)
    date=models.DateField( auto_now=False, auto_now_add=False)
    time=models.DateTimeField( auto_now=False, auto_now_add=False)
    online_time=models.DateTimeField( auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.admin_id

class Payport(models.Model):
    port=models.CharField( max_length=50)
class Payment(models.Model):
    payment_time=models.DateTimeField( auto_now=False, auto_now_add=False)
    payport_id=models.OneToOneField(Payport, on_delete=models.CASCADE)
    users_id=models.ForeignKey(Users, on_delete=models.CASCADE) 
    payment_amount=models.IntegerField()
class Request_type(models.Model):
    type=models.CharField( max_length=50)   
    price=models.IntegerField()

class Request(models.Model):
    request_type_id=models.OneToOneField(Request_type, on_delete=models.CASCADE)
    request_date=models.DateField( auto_now=False, auto_now_add=False)
    request_time=models.DateTimeField( auto_now=False, auto_now_add=False)
    request_image=models.CharField( max_length=1000)
    comment=models.CharField( max_length=1200)
    admin_dicision=models.CharField( max_length=1200)
    admin_comment=models.CharField( max_length=1200)
    user_id=models.ForeignKey(Users, on_delete=models.CASCADE)
    admin_id=models.ForeignKey(Admins, on_delete=models.CASCADE)
    def __str__(self):
        return self.request_type_id
class Locations(models.Model):
    location=models.CharField( max_length=1200)#!??

class Driving_fine(models.Model):
    type=models.CharField( max_length=70)
    price=models.IntegerField()
class Drivers_fined(models.Model):
    users_id=models.ForeignKey(Users, on_delete=models.CASCADE)
    car_photo=models.ImageField( upload_to='car_image', height_field=None, width_field=None, max_length=None)
    car_tag=models.CharField(max_length=50)
    location_id=models.ForeignKey(Locations, on_delete=models.CASCADE)
    driving_fine_id=models.ForeignKey(Driving_fine, on_delete=models.CASCADE)
    date=models.DateField( auto_now=False, auto_now_add=False)
    time=models.DateTimeField( auto_now=False, auto_now_add=False)