from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table="category"

    def __str__(self):
        return self.name




class Subcategory(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    class Meta:
        db_table="subcategory"

    def __str__(self):
        return self.name


class Plan(models.Model):
    name=models.CharField(max_length=30)
    class Meta:
        db_table="plan"

    def __str__(self):
        return self.name



class Service(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=1000)
    simage=models.ImageField(upload_to ='images',default="")
    plan=models.ManyToManyField(Plan)
    # plan_price=models.IntegerField()
    ratings=models.IntegerField()
    subcategory=models.ManyToManyField(Subcategory)
    # category=models.ManyToManyField(Category)

    class Meta:
        db_table="service"

    def __str__(self):
        return self.name

class PlanPrice(models.Model):
    plan=models.ForeignKey(Plan,on_delete=models.CASCADE)
    service=models.ForeignKey(Service,on_delete=models.CASCADE)
    price=models.IntegerField()


    class Meta:
        db_table="plan_price"
        unique_together = ('service', 'plan',)

    def __str__(self):
        return " ".join([str(self.plan),str(self.price)])
# Create your models here.
