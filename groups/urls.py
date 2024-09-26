from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudyGroupViewSet

router = DefaultRouter()
router.register(r'/group', StudyGroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
