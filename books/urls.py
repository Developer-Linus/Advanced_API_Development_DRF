from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import AuthorViewSet, BookViewSet

router = DefaultRouter()
router.register(r'authorss', AuthorViewSet)
router.register(r'bookss', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]