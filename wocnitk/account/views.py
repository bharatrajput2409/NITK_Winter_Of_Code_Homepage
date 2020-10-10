from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.db import IntegrityError
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.http import JsonResponse
from django.core.mail import send_mail,EmailMessage
from . models import userdetails ,branch


# Create your views here.
def home(request):
    print("bharat")
    return render(request ,'account/home.html')

def projects(request):
    print("bharat")
    return render(request ,'account/projects.html')

def login(request):
    if request.method=="POST":
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect("/")
        else:
            messages.add_message(request,messages.ERROR,"wrong credential !")
            return HttpResponseRedirect("/login")
    else:
        login=1
        return render(request ,'account/login.html',{'login':login})


def register(request):
    if request.method=="POST":
        fname=request.POST.get('fname','')
        lname=request.POST.get('lname','')
        username=request.POST.get('username','')
        password1=request.POST.get('password1','')
        password2=request.POST.get('password2','')
        email=request.POST.get('email','')
        branchname=request.POST.get('branch','')
        batch=request.POST.get('batch','2020')
        print(username)
        if password1!=password2:
            messages.add_message(request,messages.ERROR,"Both password should be same !")
            return redirect('/register')
        try:
            branch_id=branch.objects.get(name=branchname)
        except branch.DoesNotExist:
            messages.add_message(request,messages.ERROR,"Entre a valid branch !")
            return redirect('/register')
        try:
            User.objects.get(username=username)
            messages.add_message(request,messages.ERROR,"Username already taken !")
            return redirect('/register')
        except User.DoesNotExist:
            obj=User.objects.create_user(first_name=fname,last_name=lname,username=username,password=password1,email=email)
        userobj=userdetails()
        userobj.branch=branch_id
        userobj.user=obj
        userobj.batch=batch
        userobj.save()
        user=auth.authenticate(username=username,password=password1)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect("/")
        return redirect("/login")
    else:
        login=0
        return render(request ,'account/login.html',{'login':login})


def reportbug(request):
    content=request.POST.get('message','')
    subject='Bug report for WoC-NITK!'
    reciverlist=['bharatrajput2409@gmail.com','nutboltcode@gmail.com']
    send_mail(subject,content,'bharatsinghnitk@gmail.com',reciverlist,fail_silently=False)
    return redirect("/")

def logout(request):
    auth.logout(request)
    return redirect("/")


def checkforavailableusername(request,username):
    try:
        User.objects.get(username=username)
        return HttpResponse("1")
    except User.DoesNotExist:
        return HttpResponse("0")

def profile(request):
    userdetail=userdetails.objects.get(user=request.user)
    return render(request,'account/profile.html',{'userdetails':userdetail})

def orgs(request):
    return render(request,'account/orgs.html')