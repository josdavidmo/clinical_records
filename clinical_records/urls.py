"""
clinical_records URL Configuration
"""

from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from patients.views import Index
from django.conf import settings

urlpatterns = [
    url(r'^$', Index.as_view(), name="home"),
    url(r'^admin/', admin.site.urls),
    url(r'^patients/', include('patients.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
