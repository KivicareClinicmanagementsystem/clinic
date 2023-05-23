from django.urls import path
from kkarmapp import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns=[
path('home/',views.homeview.as_view()),
path('About/',views.Aboutview.as_view()),
path('boot/',views.bootview.as_view()),
path('temp/',views.tempview.as_view()),
path('renovat/',views.renovatview.as_view()),
path('form/',views.formview.as_view()),
path('clinic/',views.clinicview.as_view()),
path('contact/',views.contactview.as_view()),
path('insertcontact/',views.insertcontact),
path('blog/',views.blogview),
path('blogdetail/<int:id>',views.blogdetail),
path('faq/',views.FAQsview),
path('signup/',views.signupview),
path('login/',LoginView.as_view(),name="login"),
path('logout/',LogoutView.as_view(),name="logout"),
path('Doctor/',views.doctorview),
path('Doctordetail/<int:id>',views.Doctordetail),
path('Treatments/',views.Treatmentsview),
path('Service/',views.Serviceview.as_view()),
path('Treatmentsdetail/<int:id>',views.Treatmentsdetail),
path('Appointment/',views.Appointmentview),
path('insertAppointment/',views.insertAppointment),
path('PatientReports/',views.PatientReportsview),
path('insertSubcribe/',views.insertSubcribe),
path('updatefeedback/',views.updatefeedbackview),
path("payment/", views.order_payment, name="payment"),
path("callback/", views.callback, name="callback"),
path("paybooking/<int:id>",views.paybooking,name="paybooking"),
    
]