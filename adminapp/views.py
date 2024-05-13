from django.shortcuts import render, redirect
from fmiapp.models import Enquiry,LoginInfo,MerchantInfo,FarmerInfo,Feedback
from . models import Booking, News
import datetime

# Create your views here.
def adminhome(request):
    try:
        if request.session['userid']:
            ns=News.objects.all()
            return render(request,'adminhome.html',{'ns':ns})
    except:
        return render(request,'login.html')


def enquiries(request):
    try:
        if request.session['userid']:
            enq = Enquiry.objects.all()
            return render(request,'enquiries.html',{'enq':enq})
    except:
        return render(request,'login.html')

def booking(request):
    try:
        if request.session['userid']:
            fi=FarmerInfo.objects.all()
            return render(request,'booking.html',{'fi':fi})
    except:
        return render(request,'login.html')

def purchase(request):
    try:
        if request.session['userid']:
            bk=Booking.objects.all()
            return render(request,'purchase.html',{'bk':bk})
    except:
        return render(request,'login.html')


def changepassword(request):
    try:
        if request.session['userid']:
            return render(request,'changepassword.html')
    except:
        return render(request,'login.html')

def logout(request):
    request.session['userid']=None
    msg='you have logged out'
    return render(request,'login.html',{'msg':msg})


def book(request,ano):
    fi=FarmerInfo.objects.get(aadharno=ano)
    return render(request,'book.html',{'fi':fi})

def pbook(request):
    name=request.POST['name']
    address=request.POST['address']
    contactno=request.POST['contactno']
    aadharno=request.POST['aadharno']
    noofpacket=int(request.POST['noofpacket'])
    duration=int(request.POST['duration'])
    rate=int(request.POST['rate'])
    advance=int(request.POST['advance'])
    totalamt=noofpacket*duration*rate
    restamt=totalamt-advance
    bookingdate=datetime.datetime.today()
    b=Booking(name=name,address=address,contactno=contactno,aadharno=aadharno,noofpacket=noofpacket,duration=duration,rate=rate,totalamt=totalamt,advance=advance,restamt=restamt,bookingdate=bookingdate)
    b.save()
    msg='Booking is done'
    return redirect('adminapp:booking')
def viewbook(request,ano):
    res=Booking.objects.get(aadharno=ano)
    return render(request,'viewbook.html',{'res':res})


def deleteenq(req,id):
    e=Enquiry.objects.get(id=id)
    e.delete()
    return redirect('adminapp:enquiries')


def addnews(req):
    newstext=req.POST['newstext']
    newsdate=datetime.datetime.today()
    ns=News(newstext=newstext,newsdate=newsdate)
    ns.save()
    return redirect('adminapp:adminhome')


def deletenews(req,id):
    ns=News.objects.get(id=id)
    ns.delete()
    return redirect('adminapp:adminhome')

def changepwd(req):
    oldpassword=req.POST['oldpassword']
    newpassword=req.POST['newpassword']
    confirmpassword=req.POST['confirmpassword']
    msg='Message='
    if newpassword!=confirmpassword:
        msg=msg+'New password is not matched with confirm password'
        return render(req,'changepassword.html',{'msg':msg})
    userid=req.session['userid']
    try:
        obj=LoginInfo.objects.get(userid=userid,password=oldpassword)
        LoginInfo.objects.filter(userid=userid).update(password=newpassword)
        return  redirect('adminapp:logout')

    except:
        msg=msg+'Old password is not matched'
    return render(req,'changepassword.html',{'msg':msg})


def pay(req,ano):
    obj=Booking.objects.get(aadharno=ano)
    return render(req,'pay.html',{'obj':obj})

def paid(req):
    aadharno=req.POST['aadharno']
    restamt=int(req.POST['restamt'])
    payamt=int(req.POST['payamt'])
    restamt=restamt-payamt
    Booking.objects.filter(aadharno=aadharno).update(restamt=restamt)
    return redirect('adminapp:purchase')



def feedbackmanagement(request):
    try:
        if request.session['userid']:
            feed=Feedback.objects.all()
            return render(request,'feedback.html',{'feed':feed})
    except:
        return render(request,'login.html')


