from django.shortcuts import render,redirect
from .models import User,Service,Cart,PlanPrice



def add_cart(request,sid,ppid):
    service=Service.objects.get(id=sid)
    uid=request.user.id
    user=User.objects.get(id=uid)
    planprice=PlanPrice.objects.get(id=ppid)
    c=Cart()
    c.user=user
    c.service=service
    c.planprice=planprice
    c.save()
    return redirect("/cart-view")



def cart(request,id=None):
    if id!=None:
        try:
            c=Cart.objects.get(id=id)
            c.delete()
        except:
            cartl=Cart.objects.all()

        
        
        cartl=Cart.objects.all()
        nc=len(cartl)
        context={"cartl":cartl,"nc":nc}
        return render(request,"cart_view.html",context)


        # try:
        #     c=Cart.objects.get(id=id)
        #     c.delete()
        # except:
        #     cartl=Cart.objects.all()

        # cartl=Cart.objects.all()
        # nc=len(cartl)
        # context={"cartl":cartl,"nc":nc}
        # return render(request,"cart_view.html",context)
    else:
        cartl=Cart.objects.filter(user=request.user)
        nc=len(cartl)
        sc=sum([i.planprice.price for i in cartl])
        if sc>3000:
            disc=sc*0.05
        else:
            disc=sc*0.02
        fp=sc-disc
        context={"cartl":cartl,"sc":sc,"disc":disc,"fp":fp,"nc":nc}
        return render(request,"cart_view.html",context)

# Create your views here.
