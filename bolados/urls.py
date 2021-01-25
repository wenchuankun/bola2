from django.urls import path
from bolados import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.Inicio, name="Inicio"),
    path('Producto', views.Producto, name="Producto"),
    path('Pedido', views.Pedido, name="Pedido"),
    path('Cliente', views.Cliente, name="Cliente"),
    path('Login', views.Login, name="Login"),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
