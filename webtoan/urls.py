from django.contrib import admin
from django.urls import path, include

# 👇 THÊM 2 DÒNG NÀY
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
]

# 👇 THÊM DÒNG NÀY Ở CUỐI
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)