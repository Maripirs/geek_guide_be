
from django.contrib import admin
from django.urls import path, include
from geeks.views import *
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()
router.register(r'game', SingleGameView)
router.register(r'games', AllGamesView)
router.register(r'section', SectionView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
