from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, IngresoViewSet

router = DefaultRouter()
router.register(r"usuarios", UsuarioViewSet, basename="usuario")
router.register(r"ingresos", IngresoViewSet, basename="ingreso")

urlpatterns = [
    path("", include(router.urls)),
]
