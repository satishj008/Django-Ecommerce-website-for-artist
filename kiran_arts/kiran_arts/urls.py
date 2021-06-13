from django.contrib import admin
from django.urls import path,include
from accounts.views import home
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("",home),
    path('admin/', admin.site.urls),
    path("acc-",include(("accounts.urls","accounts"),namespace="accounts")),
    path("prod-",include(("products.urls","products"),namespace="products")),
    path("cart-",include(("cart.urls","cart"),namespace="cart")),
    path("order-",include(("order.urls","order"),namespace="order")),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
