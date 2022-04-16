from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('create', index),
    path('legends', index),
    path('posts', index),
    path('posts/<int:id>', index),
]
