from django.contrib import admin
from . models import FarmerInfo, MerchantInfo, LoginInfo, Enquiry,Feedback


# Register your models here.
admin.site.register(FarmerInfo)
admin.site.register(MerchantInfo)
admin.site.register(LoginInfo)
admin.site.register(Enquiry)
admin.site.register(Feedback)