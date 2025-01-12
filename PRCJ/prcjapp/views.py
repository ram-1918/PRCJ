from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def base(request):
    return render(request,'home.html')

def haramfunc(request):
    #h=item_models.objects.filter(item_id="Haram001",item_type="haram")
    #print(h)

    harams=item_models.objects.filter(item_type="haram")
    return render(request,'haram.html',{'res':harams})

def banglefunc(request):    
    bangles=item_models.objects.filter(item_type="bangle")
    #print(bangles)
    return render(request,'bangles.html',{'res':bangles})

def chainfunc(request):
    chains=item_models.objects.filter(item_type="chains")
    #print(chains)
    return render(request,'chains.html',{'res':chains})

def wishlists(request,id):
    devicename=request.COOKIES['device']
    print("success")
    print(id)
    item_id=request.GET.get('post_id',False)
    item_type=item_id[:-3].lower()

    wishedlist=item_models.objects.get(item_id=item_id,item_type=item_type)
    wishedlist.item_status=id
    wishedlist.save()

    wishlist.objects.create(devicename=devicename,item_id=item_id,item_type=item_type,item_status=id)

    return render(request,'wishlists.html')

def display(request):
    devicename=request.COOKIES['device']
    d=[]
    try:
        wishlist.objects.get(devicename=devicename,item_status=0).delete()
    except:
        pass
    wishedlist=wishlist.objects.filter(devicename=devicename,item_status=1)
    #if wishlist.objects.get(devicename=devicename,item_status=1)


    for i in wishedlist:
        w=item_models.objects.filter(item_id=i.item_id,item_type=i.item_type)
        d.append(w)
    #print(d)
    return render(request,'wishlists.html',{'res':d})



def register(request):
    username=''
    successmsg=''
    usernameerr=''
    passworderr=''
    success=''
    user=''
    suc=0
    if request.method=='POST':
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if len(password1)>6:
                if password1[0].isalpha():
                    if User.objects.filter(username=username).exists(): 
                        #messages.info(request,"USERNAME EXISTS")
                        usernameerr="Username Taken!"
                    elif len(username)<4 or len(username)>14:
                        usernameerr="Username should contain charecters between 4 and 14"
                    elif not username.isalnum():
                        usernameerr="Username should contain only letters and numbers"
                    else:
                        user=User.objects.create_user(username=username,password=password1)
                        user.save()
                        success="Registered Successfully"
                        user=username.title()
                        suc=1
                        print(suc,user,success)
                        return render(request,"home.html",{"registered":suc,"successmsg":success,"user":user})
                        #return redirect('/',s="suc")
                else:
                    passworderr="password should start with a charecter"
            else:
                passworderr="Password should contain more than 6 charecters"
        else:
            #messages.info(request,"PASSWORDS MISMATCH")
            passworderr="Password Mismatch!"
        
    msgs={"usernameerr":usernameerr,"passworderr":passworderr,"successmsg":successmsg}

    return render(request,"register.html",{"username":username,"usernameerr":usernameerr,"passworderr":passworderr})

def login(request):
    loginerr=''
    username=''
    registered=0
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
    user=User.objects.all()
    for i in user:
        #print(i.password)
        if i.username==username:
            registered=1
            return render(request,'home.html',{"registered":registered,"user":username.capitalize})
    else:
        loginerr="Username or Password entered is incorrect"
        
    return render(request,"login.html",{"loginerr":loginerr})



    

