from django.urls import path
from .views import (
    PostListAPIView
)
from rest_framework.routers import SimpleRouter
urlpatterns = [
    path('',PostListAPIView.as_view(),name='post_list_api')
]
"""router=SimpleRouter()
router.register('',PostAPIView,basename='post_api')
urlpatterns+=router.urls"""

