from django.contrib import admin
from kkarmapp.models import*
# Register your models here.

@admin.register(content)
class contentadmin(admin.ModelAdmin):
    list_display=('firstname','email','subject','message',)

@admin.register(product)
class productadmin(admin.ModelAdmin):
    pass

@admin.register(blog)
class blogadmin(admin.ModelAdmin):
    pass

@admin.register(FAQ)
class FAQadmin(admin.ModelAdmin):
    pass

@admin.register(Treatments)
class Treatmentadmin(admin.ModelAdmin):
    pass

@admin.register(Doctor)
class Doctoradmin(admin.ModelAdmin):
    pass

@admin.register(Appoinment)
class Appoinmentadmin(admin.ModelAdmin):
     list_display=('name','Gender','treatmentid','Dob','address','phoneno','Appoinmenttime','Appoinmentdate','doctorid','feedback',)

@admin.register(PatientReports)
class PatientReportsadmin(admin.ModelAdmin):
    pass

@admin.register(Subcribe)
class Subcribeadmin(admin.ModelAdmin):
    pass


@admin.register(Ordernow)
class Ordernowadmin(admin.ModelAdmin):
    pass
