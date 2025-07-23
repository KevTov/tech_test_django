from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Usuario, Ingreso
from .serializers import UsuarioSerializer, IngresoSerializer


def home(request):
    return HttpResponse("Bienvenido a la API. Use /core/ para acceder a los endpoints.")


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"detail": "Usuario y sus ingresos eliminados correctamente"},
            status=status.HTTP_204_NO_CONTENT,
        )


class IngresoViewSet(viewsets.ModelViewSet):
    serializer_class = IngresoSerializer
    queryset = Ingreso.objects.none()

    def get_queryset(self):
        queryset = Ingreso.objects.all()
        usuario_id = self.request.query_params.get("usuario_id")
        if usuario_id:
            queryset = queryset.filter(usuario_id=usuario_id)
        return queryset

    def create(self, request, *args, **kwargs):
        usuario_id = request.data.get("usuario")
        if not usuario_id:
            return Response(
                {"error": "Se requiere el ID del usuario"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        get_object_or_404(Usuario, pk=usuario_id)
        return super().create(request, *args, **kwargs)
