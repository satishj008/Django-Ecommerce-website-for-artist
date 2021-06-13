from django.db import models
from accounts.models import User
from products.models import Service,Plan,PlanPrice

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    service=models.ForeignKey(Service,on_delete=models.CASCADE)
    # plan=models.ForeignKey(Plan,on_delete=models.CASCADE)
    planprice=models.ForeignKey(PlanPrice,on_delete=models.CASCADE)

# Create your models here.
