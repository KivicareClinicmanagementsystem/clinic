from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
import datetime
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _
from .constants import PaymentStatus

# Create your models here.
class content(models.Model):
    firstname=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=200)
    message=models.TextField()
    class Meta:
        db_table="content"

class product(models.Model):
    name=models.CharField(max_length=100)
    mrp=models.FloatField()
    sellingprice=models.FloatField()
    description=models.TextField()
    photo=models.ImageField(upload_to='product/')
    class Meta:
        db_table="product"
    def __str__(self):
      return self.name    
    
class blog(models.Model):
    title=models.CharField(max_length=200)
    description=HTMLField()
    photo=models.ImageField(upload_to='blog/')
    postby=models.CharField(max_length=50,default="Admin")
    poston=models.DateField(default=datetime.date.today())
    class Meta:
        db_table="blog"
    def __str__(self):
        return self.title
    
    
class FAQ(models.Model):
    question=models.TextField()
    answer=models.TextField()
    class Meta:
        db_table="FAQ"
    def __str__(self):
        return self.question
    

class Treatments(models.Model):
    name=models.CharField(max_length=100)
    description=HTMLField(default="")
    photo=models.ImageField(upload_to='Treaments/')
    class Meta:
        db_table="Treatments"
    def __str__(self):
      return self.name
    
class Doctor(models.Model):
    name=models.CharField(max_length=100)
    treatmentid=models.IntegerField()
    qualification=models.CharField(max_length=100)
    description=HTMLField(default="")
    specialist=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='Doctor/')
    class Meta:
        db_table="Doctor"
    def __str__(self):
      return self.name  


class Appoinment(models.Model):
    name=models.CharField(max_length=100)
    Gender=models.CharField(max_length=20,)
    treatmentid=models.ForeignKey(Treatments,on_delete=models.CASCADE,blank=True,null=True)
    Dob=models.DateField()
    address=models.CharField(max_length=1024)
    phoneno=models.BigIntegerField()
    Appoinmenttime=models.TimeField()
    Appoinmentdate=models.DateField()
    doctorid=models.ForeignKey(Doctor,on_delete=models.CASCADE,blank=True,null=True)
    feedback=models.TextField()
    class Meta:
        db_table="Appoinment"
    def __str__(self):
        return self.name    

class PatientReports(models.Model):
    Userid=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    Report=models.FileField(upload_to='PatientReports/')
    DoctorFeedback=models.TextField(default="")
    PatientFeedback=models.TextField(default="")
    Report_date=models.DateField(auto_now=True)
    class Meta:
        db_table="PatientReports"
    def __str__(self):
        return self.DoctorFeedback
    
class Subcribe(models.Model):
    emailid=models.CharField(max_length=100,default="")
    class Meta:
        db_table="Subcribe"
    def __str__(self):
        return self.emailid
    
class Ordernow(models.Model):
    name = CharField(_("Customer Name"), max_length=254, blank=False, null=False)
    amount = models.FloatField(_("Amount"), null=False, blank=False)
    status = CharField(
        _("Payment Status"),
        default=PaymentStatus.PENDING,
        max_length=254,
        blank=False,
        null=False,
    )
    provider_order_id = models.CharField(
        _("Order ID"), max_length=40, null=False, blank=False
    )
    payment_id = models.CharField(
        _("Payment ID"), max_length=36, null=False, blank=False
    )
    signature_id = models.CharField(
        _("Signature ID"), max_length=128, null=False, blank=False
    )
    Appointmentid=models.ForeignKey(Appoinment,on_delete=models.CASCADE,blank=True,null=True,related_name="issues")

    def __str__(self):
        return f"{self.id}-{self.name}-{self.status}"



    
      
