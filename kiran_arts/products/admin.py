from django.contrib import admin
from .models import Category,Subcategory,Plan,Service,PlanPrice

class CategoryAdmin(admin.ModelAdmin):
    list_display=["id","name"]

admin.site.register(Category,CategoryAdmin)
# Register your models here.
class SubcategoryAdmin(admin.ModelAdmin):
    list_display=["id","name","category"]
    list_filter=["category"]

admin.site.register(Subcategory,SubcategoryAdmin)


class PlanAdmin(admin.ModelAdmin):
    list_display=["id","name"]

admin.site.register(Plan,PlanAdmin)

class PlanPriceAdmin(admin.ModelAdmin):
    list_display=["id","plan","service","price"]
    list_filter=["service","plan"]

admin.site.register(PlanPrice,PlanPriceAdmin)

class ServiceAdmin(admin.ModelAdmin):
    fields=["name","description","simage",'plan',"ratings","subcategory"]
    list_display=('get_subcategory',)

    def get_subcategory(self,obj):
        return "\n".join([s.name for s in obj.subcategory.all()])

admin.site.register(Service,ServiceAdmin)
