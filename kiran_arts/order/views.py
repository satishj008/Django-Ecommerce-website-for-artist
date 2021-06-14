from django.shortcuts import render,redirect
from cart.models import User,Service,Cart,PlanPrice
from .models import Order
from products.views import cart_count


def conv(st):
  spl=st.split(",")
  sd=[]
  for i in spl:
    p=""
    for j in i:
      if j.isdigit():
        p+=j
    sd.append(int(p))
  print(sd)
  s=[]
  t=[]
  for i in range(len(sd)):
    t.append(sd[i])
    if i%2 != 0 and i!=0:
      s.append(t)
      t=[]
  return s



def order_view(request):
    nc=cart_count(request)
    sel=Service.objects.all()
    ppl=PlanPrice.objects.all()
    ol=Order.objects.filter(user=request.user).order_by('orderdate').reverse()
    for i in ol:
        i.service_price=conv(i.service_price)
        print(">>>>>",i.service_price)
    context={"ol":ol,"sel":sel,"ppl":ppl,'nc':nc}
    return render(request,"order_view.html",context)

def checkout_view(request):
    cartl=Cart.objects.filter(user=request.user)
    nc=len(cartl)
    sc=sum([i.planprice.price for i in cartl])
    if sc>3000:
        disc=sc*0.05
    else:
        disc=sc*0.02
    fp=sc-disc
    if request.method=="POST":
        order=Order()
        order.user=User.objects.get(id=request.user.id)
        order.totalbill=fp
        order.ship_first_name=request.user.first_name
        order.ship_last_name=request.user.last_name
        order.ship_email=request.user.email
        order.ship_contact=request.POST.get("number")
        order.ship_country=request.POST.get("country_name")
        order.ship_state=request.POST.get("state-province")
        order.ship_address=request.POST.get("address")
        order.ship_pin=request.POST.get("post")
        order.payment=request.POST.get("payment")
        s_p_lst=[]
        for i in cartl:
            s_p_lst.append([i.service.id,i.planprice.id])
        order.service_price=s_p_lst
        order.save()
        for i in cartl:
            i.delete()
        return redirect("/")
    else:
        f=User.objects.get(id=request.user.id)
        context={"cartl":cartl,"sc":sc,"disc":disc,"fp":fp,"nc":nc,"form":f}
        return render(request,"checkout_view.html",context)
