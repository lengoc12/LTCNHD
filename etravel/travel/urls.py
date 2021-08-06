from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
#from .admin import admin_site


router = DefaultRouter()
router.register('travel', views.TourViewSet)

urlpatterns = [
    path('', include(router.urls))
    #path('', views.index, name='index'),
    #path('admin/', admin_site.urls),
]