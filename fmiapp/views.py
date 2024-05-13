from django.shortcuts import render, redirect, reverse
from .models import FarmerInfo,MerchantInfo, LoginInfo, Enquiry,Feedback
import datetime
from adminapp.models import News

# Create your views here.
def index(request):
    ns=News.objects.all()
    return render(request,'index.html',{'ns':ns})
def about(request):
    ns = News.objects.all()
    return render (request, 'about.html',{'ns':ns})
def farmerreg (request):
    ns=News.objects.all()
    return render(request,'farmerreg.html',{'ns':ns})
def merchantreg (request):
    ns=News.objects.all()
    return render(request, 'merchantreg.html',{'ns':ns})
def login(request):
    ns = News.objects.all()
    return render(request, 'login.html',{'ns':ns})
def contact (request):
    ns = News.objects.all()
    return render(request, 'contact.html',{'ns':ns})

def freg(request):
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    contact=request.POST['contactno']
    aadhar=request.POST['aadharno']
    regdate=datetime.datetime.today()
    fi=FarmerInfo(name=name,gender=gender,address=address,contactno=contact,aadharno=aadhar,regdate=regdate)
    fi.save()
    msg='You have registered successfuly'
    return render(request,'farmerreg.html',{'msg':msg})






def mreg(request):
    name=request.POST['name']
    gender=request.POST['gender']
    firmname=request.POST['firmname']
    firmaddress=request.POST['firmaddress']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    aadharno=request.POST['aadharno']
    panno=request.POST['panno']
    gstno=request.POST['gstno']
    regdate=datetime.datetime.today()
    mi=MerchantInfo(name=name,gender=gender,firmname=firmname,firmaddress=firmaddress,contactno=contactno,emailaddress=emailaddress,aadharno=aadharno,panno=panno,gstno=gstno,regdate=regdate)
    mi.save()
    msg='you have registered successfully'
    return render(request,'merchantreg.html',{'msg':msg})

def validate(request):
    userid=request.POST['userid']
    password=request.POST['password']
    try:
        obj=LoginInfo.objects.get(userid=userid,password=password)
        request.session['userid']=userid
        return redirect(reverse('adminapp:adminhome'))
    except:
        msg='Invalid User'
    return render(request,'login.html',{'msg':msg})

def saveenq(request):
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    enquirytext=request.POST['enquirytext']
    enquirydate=datetime.datetime.today()
    enq=Enquiry(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,enquirytext=enquirytext,enquirydate=enquirydate)
    enq.save()
    msg='Your enquiry is submitted'
    return render(request,'contact.html',{'msg':msg})


def feedback(req):
    ns = News.objects.all()
    return render(req,'fmifeedback.html',{'ns':ns})





def feed(request):
    name=request.POST['name']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    feedbacktext=request.POST['feedbacktext']
    feedbackdate=datetime.datetime.today()
    fe=Feedback(name=name,contactno=contactno,emailaddress=emailaddress,feedbacktext=feedbacktext,feedbackdate=feedbackdate)
    fe.save()
    msg='Your Feedback is submitted. !!Thanks!!'
    return render(request,'fmifeedback.html',{'msg':msg})

