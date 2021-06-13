from django.shortcuts import render,redirect
from django.contrib import messages as msg
from .models import UserForm
from django.contrib.auth import login,logout,authenticate
from products.models import Category,Subcategory,Service,Plan,PlanPrice
from cart.views import Cart


def cart_count(request):
    if request.user.is_authenticated:
        nc=len(Cart.objects.filter(user=request.user))

    else:
        nc=0

    return nc


def home(request):

    nc=cart_count(request)
    cl=Category.objects.all()
    sl=Subcategory.objects.all()
    ppl=PlanPrice.objects.all()

    sel=Service.objects.all()
    lst=[]
    serl=[]
    sm=set()
    for i in sel:
        for j in i.subcategory.all():
            sm.add(j.category.name)
    for k in list(sm):
        ser=Service.objects.filter(subcategory__category__name=k).distinct()
        serl.append([ser,k])

    pl=Plan.objects.all()
    ppl=PlanPrice.objects.all()
    context={'cl':cl,"sl":sl,"sel":sel,"pl":pl,"ppl":ppl,"serl":serl,"nc":nc,"ppl":ppl}
    return render(request,"home.html",context)


def add_user(request):
    nc=cart_count(request)
    if request.method=="POST":
        f=UserForm(request.POST)
        f.save()
        return redirect("/")
    else:
        f=UserForm
        d={'form':f,"nc":nc}
        return render(request,"register.html",d)


def login_view(request):
    nc=cart_count(request)
    if request.method=="POST":
        uname=request.POST.get("uname")
        passw=request.POST.get("passw")
        u=authenticate(request,username=uname,password=passw)
        if u is not None:
            login(request, u)
            return redirect("/")

        else:
            msg.error(request,"Invalid username & password")
            return render(request,"login.html",{'nc':nc})

    else:

        return render(request,"login.html",{'nc':nc})


def logout_view(request):
    logout(request)
    return redirect("/")

# Create your views here.
