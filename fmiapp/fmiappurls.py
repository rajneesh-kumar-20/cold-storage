from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('farmerreg/',views.farmerreg,name='farmerreg'),
    path('merchantreg/',views.merchantreg,name='merchantreg'),
    path('login/',views.login,name='login'),
    path('contact/',views.contact,name='contact'),
    path('freg/',views.freg,name='freg'),
    path('mreg/',views.mreg,name='mreg'),
    path('validate/',views.validate,name='validate'),
    path('saveenq/',views.saveenq,name='saveenq'),
    path('feedback/',views.feedback,name='feedback'),
    path('feed/',views.feed,name='feed'),

]