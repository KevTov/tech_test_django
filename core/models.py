from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    groups = models.ManyToManyField(Group, related_name="core_usuario_set", blank=True)
    user_permissions = models.ManyToManyField(
        Permission, related_name="core_usuario_set", blank=True
    )

    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


class Ingreso(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_entrada = models.DateTimeField()
    fecha_salida = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Ingreso"
        verbose_name_plural = "Ingresos"

    def save(self, *args, **kwargs):
        if not self.fecha_entrada:
            self.fecha_entrada = timezone.now()
        if not self.fecha_salida:
            self.fecha_salida = self.fecha_entrada + timezone.timedelta(hours=5)
        super().save(*args, **kwargs)
