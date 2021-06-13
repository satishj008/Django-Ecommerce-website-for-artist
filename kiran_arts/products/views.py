from django.shortcuts import render
from products.models import Category,Subcategory,Service,Plan,PlanPrice
from cart.models import Cart

def cart_count(request):
    if request.user.is_authenticated:
        nc=len(Cart.objects.filter(user=request.user))
    else:
        nc=0

    return nc

def filter_by_cat(request,id=None):
    cl=Category.objects.all()
    sl=Subcategory.objects.all()
    pl=Plan.objects.all()
    ppl=PlanPrice.objects.all()
    nc=cart_count(request)
    if id==None:
        sel=Service.objects.all()
    else:
        sel=Service.objects.filter(subcategory=id)

    context={'cl':cl,"sl":sl,"sel":sel,"pl":pl,"nc":nc,"ppl":ppl}
    return render(request,"service_view.html",context)

def search_match(s,i):
    if s.lower() in i.name.lower() or s.lower() in i.description.lower() :
        return True
    return False

def search(request):
    s=request.GET.get("search")
    cl=Category.objects.all()
    sl=Subcategory.objects.all()
    pl=Plan.objects.all()
    ppl=PlanPrice.objects.all()
    nc=cart_count(request)
    seltemp=Service.objects.all()
    sel=[i for i in seltemp if search_match(s,i)]
    context={'cl':cl,"sl":sl,"sel":sel,"pl":pl,"nc":nc,"ppl":ppl}
    return render(request,"service_view.html",context)



def gig_view(request,id=None):
    cl=Category.objects.all()
    sl=Subcategory.objects.all()
    pl=Plan.objects.all()
    ppl=PlanPrice.objects.filter(service=id)
    sel=Service.objects.filter(id=id)
    nc=cart_count(request)
    context={'cl':cl,"sl":sl,"sel":sel,"pl":pl,'ppl':ppl,"nc":nc}

    return render(request,"gig_view.html",context)
# Create your views here.
