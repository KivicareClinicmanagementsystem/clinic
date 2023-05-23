from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from kkarmapp.forms import *

from django.contrib.auth import login
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import razorpay
from django.http import HttpResponse

def order_payment(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        orderid=request.POST.get("provider_order_id")
        bookingid=request.POST.get("bookingid")
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        razorpay_order = client.order.create(
            {"amount": float(amount) * 100, "currency": "INR", "payment_capture": "1"}
        )
        order = Ordernow.objects.create(
            name=name, amount=amount, provider_order_id=razorpay_order['id'],Appointmentid_id=bookingid
        )
        order.save()
        return render(
            request,
            "payment.html",
            {
                "callback_url": "http://127.0.0.1:8000/callback/",
                "razorpay_key": settings.RAZORPAY_KEY_ID,
                "order": order,
            },
        )
    return render(request, "payment.html")


@csrf_exempt
def callback(request):
    
    razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))
    #    return client.utility.verify_payment_signature(response_data)

    if request.method == "POST":
        try:
            payment_id = request.POST.get("razorpay_payment_id", "")
            provider_order_id = request.POST.get("razorpay_order_id", "")
            signature_id = request.POST.get("razorpay_signature", "")
            params_dict={
                'razorpay_order_id':provider_order_id,
                'razorpay_payment_id':payment_id,
                'razorpay_signature':signature_id

            }
            print(params_dict)
            try:
                order = Ordernow.objects.get(provider_order_id=provider_order_id)
            except:
                return HttpResponse("505 not found inner")
            order.payment_id = payment_id
            order.signature_id = signature_id
            order.save()
            
            result=razorpay_client.utility.verify_payment_signature(params_dict)
            
            if result==True:
                amount=int(order.amount)
                
                try:
                   
                    '''res=razorpay_client.payment.capture(payment_id,{
                        "amount" : amount,
                        "currency" : "INR"
                        })
                    print(res)'''
                    order.status=PaymentStatus.SUCCESS
                    order.save()
                    return render(request, "sucess.html")
                except:
                   
                    order.status=PaymentStatus.FAILURE
                    order.save()
                    return render(request, "failure.html")
            else:
                
                order.status=PaymentStatus.FAILURE
                order.save()
                return render(request, "failure.html")
        except:
            return HttpResponse("505 not found here")
        
# Create your views here.

class homeview(TemplateView):
    template_name="homepage.html"
class Aboutview(TemplateView):
    template_name="About.html"
class bootview(TemplateView):
    template_name="boot.html" 
class tempview(TemplateView):
    template_name="temp.html"
class renovatview(TemplateView):
   template_name="renovat.html"
class formview(TemplateView):
    template_name="form.html"
class clinicview(TemplateView):
    template_name="clinic.html"
class contactview(TemplateView):
    template_name="contact.html"
class Serviceview(TemplateView):
    template_name="Service.html"    
def insertcontact(request):
    if request.method=='POST':
        form=contentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/clinic/')
    else:
        form=contentform()
        return render(request,"contact.html",{'form:form'})
    
def blogview(request):
    big=blog.objects.all()
    return render(request,"blog.html",{'big':big})   

def blogdetail(request,id):
    blg=blog.objects.get(id=id)
    return render(request,"blogdetail.html",{'blg':blg}) 

def FAQsview(request):
    f=FAQ.objects.all()
    return render(request,"FAQ.html",{'f':f})


def signupview(request):
    if request.method=='POST':
        form=signupform(request.POST)
        if form.is_valid():
            User=form.save()
            login(request,User)
            return redirect('/blogs/')
    else:
        form=signupform()
    return render(request,"registration/signup.html",{'form':form})   


def doctorview(request):
    d=Doctor.objects.all()
    return render(request,"Doctor.html",{'d':d})

def Doctordetail(request,id):
    d=Doctor.objects.get(id=id)
    return render(request,"Doctordetail.html",{'d':d}) 


def Treatmentsview(request):
    T=Treatments.objects.all()
    return render (request,"Treatments.html",{'T':T})

def Treatmentsdetail(request,id):
    T=Treatments.objects.get(id=id)
    return render(request,"Treatmentsdetail.html",{'T':T}) 


def insertAppointment(request):
    if request.method=='POST':
        form=Appointmentform(request.POST)
        if form.is_valid():
            obj=form.save()
            id=obj.pk
            return redirect('paybooking',id=id)
    else:
        form=Appointmentform()
    return render(request,"Appointment.html",{'form':form})

def paybooking(request,id):
    b=Appoinment.objects.get(id=id)
    return render(request,"paybooking.html",{'b':b})


def Appointmentview(request):
    t=Treatments.objects.all()
    d=Doctor.objects.all()
    return render(request,"Appointment.html",{'t':t,'d':d})

def PatientReportsview(request):
    p=PatientReports.objects.filter(Userid_id=request.user.id)
    return render(request,"PatientReports.html",{'p':p})

def insertSubcribe(request):
    if request.method=='POST':
        form=Subcribeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/clinic/')
    else:
        form=Subcribeform()
    return render(request,"base.html",{'form':form})

def updatefeedbackview(request):
    id=request.POST.get("id")
    PatientFeedback=request.POST.get("PatientFeedback")
    obj=PatientReports.objects.get(id=id)
    obj.PatientFeedback=PatientFeedback
    obj.save()
    return redirect('/PatientReports/')



