
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Just_one_fieldViewSet,Model3ViewSet,Model4ViewSet,Model5ViewSet,Model6ViewSet
router = DefaultRouter()
router.register('model4', Model4ViewSet )
router.register('just_one_field', Just_one_fieldViewSet )
router.register('model5', Model5ViewSet )
router.register('model3', Model3ViewSet )
router.register('model6', Model6ViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
