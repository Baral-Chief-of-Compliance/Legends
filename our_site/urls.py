from rest_framework import routers
from .api import Legend_IVT_ViewSet


router = routers.DefaultRouter()
router.register('Legend_IVT', Legend_IVT_ViewSet, 'Legend_IVT')


urlpatterns =  router.urls
