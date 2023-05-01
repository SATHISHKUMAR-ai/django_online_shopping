from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from django.db.models import Sum
from datetime import timedelta, datetime, tzinfo, timezone


# import sys

# the first page
def index(request):
    a=product.objects.filter(product_tittle='collection')
    b=product.objects.filter(product_tittle='special')
    c=product.objects.filter(product_tittle='blogs')
    return render(request,'front/index.html',{'a':a,'b':b,'c':c})

# the admin dasboard in admin floder
def baseadmin(request):
    return render(request,'admin/baseadmin.html')

# the login page
def login(request):
    return render(request,'login/login.html')
# the logout the id in adminpage
def logout(request):
	if request.session.has_key('user'):
		# name = request.session['user']
		del request.session['user']
		return redirect('index')
	return redirect('index') 

# the search boc and home page
def search(request):
    searc = request.POST['query']
    p=product.objects.filter( pname = searc)
    # print(p)
    context = {
        'show':p
    }
    return render(request,'front/home.html',context)


# the login at form page
def getlogin(request):
    if request.method == 'POST':
        name = request.POST['email'] 
        ps = request.POST['pwd']

        if name == "admin@gmail.com" and ps == "admin":
            request.session['user'] = name
            return HttpResponseRedirect('/baseadmin')
        
        elif formreg.objects.filter(email=name,password = ps,User_type = 2):
            request.session['user'] = name
            e=product.objects.filter(product_tittle='collection')
            d=product.objects.filter(product_tittle='special')
            c=product.objects.filter(product_tittle='blogs')
            addkarts = addkart.objects.filter(cemail=name).count()
            return render(request,'front/home.html',{'c':c,'d':d,'e':e,'addkarts':addkarts})
            
        else:
            return HttpResponseRedirect('/registration')


# the registration page in login floder
def registration(request):
    return render(request,'login/registration.html')

def save_userdata(request):
    if request.method == 'POST':
        uname = request.POST['user_name']
        umail = request.POST['nemail']
        uphone = request.POST['phone']
        upwd = request.POST['pwd']
        user1 = formreg()
        user1.name= uname
        user1.email = umail
        user1.phone = uphone
        user1.password = upwd
        user1.User_type = 2
        user1.save()

        return render(request,'login/login.html')


# the forget page in login floder
def forget(request):
    return render(request,'login/forget.html')

# the admin first add page
def firstadd(request):
    return render(request,'admin/firstadd.html')
 
#  the firstadd product in admin page
def product_save(request):
    if request.method == 'POST':
        pro = request.POST['pname']
        cir = request.POST['sale']
        phot = request.FILES['photo']
        pric = request.POST['price']
        dpric = request.POST['dprice']
        tit = request.POST['title']

        # product.objects.filter(product_tittle='collection')

        user=product()
        user.pname=pro
        user.circlesale=cir
        user.image=phot
        user.rate=pric
        user.cutrate=dpric
        user.product_tittle=tit
        user.save()

        return render(request,'admin/firstadd.html')
#  the viewadmin in admin page      
def viewadmin(request):
    # o=product.objects.filter(product_tittle='collection')
    # i=product.objects.filter(product_tittle='special')
    # p=product.objects.filter(product_tittle='blogs')
    p=product.objects.all()
    return render(request,'admin/viewadmin.html',{'view':p})

def editadmin(request,id):
    p=product.objects.filter(id=id)
    return render(request,'admin/editadmin.html',{'show':p})

# the edit  point in admin page
def changeedit(request,id):
    if request.method == 'POST':
        pro = request.POST['pname']
        cir = request.POST['sale']
        phot = request.FILES['photo']
        pric = request.POST['price']
        dpric = request.POST['dprice']
        tit = request.POST['title']
        # product.objects.filter(product_tittle='collection')
        user=product.objects.get(id=id)
        user.pname=pro
        user.circlesale=cir
        user.image=phot
        user.rate=pric
        user.cutrate=dpric
        user.product_tittle=tit
        user.save()

        return render(request,'admin/firstadd.html')
# the delete admin product     
def delete(request,id):
    try:
     user=product.objects.get(id=id)
     user.delete()
     user=product.objects.all()
     return render(request,'admin/viewadmin.html',{'view':user})
    except ObjectDoesNotExist:
     user=product.objects.all()
     return render(request,'admin/viewadmin.html',{'view':user})
# the login and home page in front sheet
def home(request):
    if request.session.has_key('user'):
        emil = request.session['user']
        e=product.objects.filter(product_tittle='collection')
        d=product.objects.filter(product_tittle='special')
        c=product.objects.filter(product_tittle='blogs')
        addkarts = addkart.objects.filter(cemail=emil).count()
    # e=product.objects.all()
    
    return render(request,'front/home.html',{'e':e,'d':d,'c':c,'addkarts':addkarts})

# the product buy view cart
def productview(request,id):
     e=product.objects.get(id=id)
    #  print(e.pname)
     return render(request,'front/productview.html',{'e':e})

# the buying product save
def buying(request):
    return render(request,'front/buying.html',{})

# the addcart product
def addcart(request,id):
    k=product.objects.get(id=id)    
    Pname=k.pname
    Image=k.image
    Rate=k.rate
    # count=request.POST['quantity']
    # tot=request.POST['total']
    gmail=request.session['user']
    Name = formreg.objects.get(email = gmail)
    emil = Name.email
    Nname = Name.name
    Phone = Name.phone 
   

    a = datetime.now()
    cdate = a.strftime("%y.%m.%d")
    cday = a.strftime("%A")
    ctime = a.strftime("%I.%M.%p")
    
    carts = addkart()
    carts.cpid=id
    carts.cemail=emil
    carts.cnam=Nname
    carts.cpname=Pname
    carts.cpimg=Image
    carts.cprice=int(Rate)
    carts.cpho=Phone
    carts.corderdate=cdate
    # carts.ctotal=tot
    # carts.cordercout=count
    carts.save()
    k = reversed(addkart.objects.filter(cemail=emil))
    a = sum(addkart.objects.filter(cemail=emil).values_list('cprice', flat=True))
    return render(request,'front/addcart.html',{'some':k,'cprice':a})
# the view_addcart in index page
def view_addcart(request):
    emil = request.session['user']
    e = reversed(addkart.objects.filter(cemail=emil))
    a = sum(addkart.objects.filter(cemail=emil).values_list('cprice', flat=True))
    # print(a,"this amount")
    return render(request,'front/addcart.html',{'some':e,'cprice':a})
# the save the data
# def cartstore(request,id):
#     if request.method== 'POST':
#         k=product.objects.get(id=id)
#         gmail=request.session['user']
#         Name = formreg.objects.get(email = gmail)
#         emil = Name.email
#         Nname = Name.name
#         Phone = Name.phone
#         ima=request.FILES['imag']
#         pri=request.POST['price']
#         tot=request.POST['total']
#         qt=request.POST['quantity']
#         pn=request.POST['pnam']
#         orderd=addkart()
#         orderd.cpname=pn
#         orderd.cpimg=ima
#         orderd.cprice=pri
#         orderd.ctotal=tot
#         orderd.cordercout=qt
#         orderd.cnam=Nname
#         orderd.cpho=Phone
#         orderd.cemail=emil
#         print(emil)
#         orderd.save()
#         k = reversed(addkart.objects.filter(cemail=emil))
#         a = sum(addkart.objects.filter(cemail=emil).values_list('cprice', flat=True))
#         return render(request,'front/addcart.html',{'some':k,'cprice':a})



# the addkart item delete option 
def addelete(request,id):
    try:
     emil = request.session['user']
     c = reversed(addkart.objects.filter(cemail=emil))
     k=addkart.objects.get(id=id)
     k.delete()
     a = sum(addkart.objects.filter(cemail=emil).values_list('cprice', flat=True))
     c=addkart.objects.all()
     return render(request,'front/addcart.html',{'some':c,'cprice':a})
    except ObjectDoesNotExist:
     emil = request.session['user']
     c = reversed(addkart.objects.filter(cemail=emil))
     a = sum(addkart.objects.filter(cemail=emil).values_list('cprice', flat=True))
     c=addkart.objects.all()
     return render(request,'front/addcart.html',{'some':c,'cprice':a})
     
