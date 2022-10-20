from unicodedata import category
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def base(request):
    return render(request,'home.html')




def haramfunc(request):
    devicename=request.COOKIES['device']
    x=wishlist.objects.filter(devicename=devicename,item_status=1)
    items=[]
    for i in x:
        items.append(i.item_id)
    print(items)
    harams=item_models.objects.filter(item_type="haram")
    for i in harams:
        i.item_id=i.item_id.upper()
        print(i.item_id)
        i.save()
    return render(request,'haram.html',{'res':harams,'items':items, 'models':True})


def banglefunc(request):    
    devicename=request.COOKIES['device']
    x=wishlist.objects.filter(devicename=devicename,item_status=1)
    items=[]
    for i in x:
        items.append(i.item_id)
    print(items)
    bangles=item_models.objects.filter(item_type="bangle")
    for i in bangles:
        i.item_id=i.item_id.upper()
        print(i.item_id)
        i.save()
    return render(request,'bangles.html',{'res':bangles,'items':items, 'models':True})






def chainfunc(request):
    devicename=request.COOKIES['device']
    x=wishlist.objects.filter(devicename=devicename,item_status=1)
    items=[]
    for i in x:
        items.append(i.item_id)
    print(items)
    chains=item_models.objects.filter(item_type="chain")
    for i in chains:
        i.item_id=i.item_id.upper()
        print(i.item_id)
        i.save()
    return render(request,'chains.html',{'res':chains,'items':items, 'models': True})





def wishlists(request,id):
    devicename=request.COOKIES['device']
    print("success")
    print(id)
    del_item_id = request.GET.get('post_id',True)
    print(del_item_id,'DNKJVBJKBSJFBJKV DJK ')
    item_id=request.GET.get('post_id',False) # GETS VALUE FROM AJAX DATA
    print(item_id,'--------------------------')
    item_type=item_id[:-3].lower()
    print(item_type)
    wishedlist=item_models.objects.get(item_id=item_id,item_type=item_type)
    wishedlist.item_status=id # UPDATES ITEM_STATUS IN THE MAIN TABLE
    wishedlist.save()

    if wishlist.objects.filter(devicename=devicename,item_id=item_id).exists():# CHECKS THE ITEM IN WISHLIST TABLE IF ALREADY EXISTS
        #p=
        wishlist.objects.get(devicename=devicename,item_id=item_id).delete()
        wishlist.objects.create(devicename=devicename,item_id=item_id,item_type=item_type,item_status=id).save()
        #p.item_status=id
        #p.save()    #IF EXISTS THEN IT GETS THAT ROW AND UPDATES THE REQUIRED VALUE AND SAVES IT
        print("ITEM ALREADY EXISTS SO IT IS DELETED FIRST AND CREATED AGAIN.")
    else:
        wishlist.objects.create(devicename=devicename,item_id=item_id,item_type=item_type,item_status=id).save()
        print("ITEM CREATED AND ADDED TO WISHLIST")

    #return HttpResponseRedirect('/wishlists') 
    #return redirect('display')
    return render(request,'wishlists.html')


def display(request):
    devicename=request.COOKIES['device']
    d=[]
    x=wishlist.objects.filter(devicename=devicename,item_status=1) # GETTING ITEMS FROM WISHLIST
    print(x)
    items=[]
    for i in x:
        items.append(i.item_id) # APPENDING TO LIST ITEMS
    print(items)
    wishedlist=wishlist.objects.filter(devicename=devicename,item_status=1) #WISHLIST TABLE FILTERS AND OUTPUTS ONLY ITEM_STATUS = 1 values
    for i in wishedlist:
        w=item_models.objects.filter(item_id=i.item_id,item_type=i.item_type)
        d.append(w)
    print(d)
    #return redirect('wishlsits.html',{'res':d,'items':items})
    return render(request,'wishlists.html',{'res':d,'items':items})



def search(request):
    searched_item = request.POST['search']
    item_ids = []
    item_types = []
    flag = 0
    for item in item_models.objects.all():
        item_ids.append(item.item_id.lower())
    
    for item in item_models.objects.all():
        item_types.append(item.item_type.lower())
    for j in item_ids:
        #print("1")
        if searched_item in j:
            #print("2")
            if len(searched_item) < 5:
                #print("3")
                for i in item_types:
                    #print("4")
                    flag = 1
                    if searched_item in i:
                        searched_item = i
                        movepage = i + 'func'
                        break
                    else:
                        print(" No search found ")
            elif searched_item == j:
                flag = 1
                category = j[:-3] + 's'
                item = item_models.objects.filter(item_type = j[:-3])
                return render(request, 'search.html', {'searched_item' : searched_item, 'category' : category, 'item':item[0], 'search' : True})
    if flag == 0:
        return render(request, 'search.html', {'search_item' : searched_item, 'search' : False})

    return redirect(movepage) #render(request, movepage,{'searched_item':searched_item})

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



    

