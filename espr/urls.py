from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('e_commerce/', include(('ecommerce.urls'), namespace='e_commerce')),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    path('main/', include('main_app.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)