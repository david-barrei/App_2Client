from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

app_name="clientes_app"

urlpatterns = [
    path('',views.inicio.as_view(), name='inicio'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




