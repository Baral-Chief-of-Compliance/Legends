from rest_framework import routers
from .api import Legend_IVT_ViewSet, Post_ViewSet, Legend_on_photo_ViewSet, CommentsViewSet


router = routers.DefaultRouter()
router.register('Legend_IVT', Legend_IVT_ViewSet, 'Legend_IVT')
router.register('Post', Post_ViewSet, 'Post')
router.register('Legend_on_photo', Legend_on_photo_ViewSet, 'Legend_on_photo')
router.register('Comments', CommentsViewSet, 'Comments')

urlpatterns =  router.urls
