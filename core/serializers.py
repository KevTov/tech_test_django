from rest_framework import serializers
from .models import Usuario, Ingreso


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ["id", "email", "first_name", "last_name", "created_at", "updated_at"]
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"required": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
        }


class IngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingreso
        fields = "__all__"
        read_only_fields = ["fecha_entrada", "fecha_salida"]
