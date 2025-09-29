from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from .models import User, Profile, Status

#Signal para manejar la creación/actualización del perfil
@receiver(post_save, sender=User)
def handle_user_profile(sender, instance, created, **kwargs):
    if created:
        # Usar transacción atómica para evitar problemas
        with transaction.atomic():
            try:
                # Intentar obtener status activo
                active_status = Status.objects.get(description='a')
            except Status.DoesNotExist:
                # Crear status por defecto si no existe
                active_status = Status.objects.create(description='a')
            
            # Crear perfil con datos básicos
            Profile.objects.create(
                user=instance,
                status=active_status,
                # Puedes agregar valores por defecto aquí si quieres
                phone=instance.phone if hasattr(instance, 'phone') else None
            )
            print(f"✅ Perfil creado automáticamente para: {instance.email}")
    else:
        # Si el usuario se actualiza, asegurarse de que tenga perfil
        try:
            instance.profile
        except Profile.DoesNotExist:
            # Si no tiene perfil, crearlo
            with transaction.atomic():
                try:
                    active_status = Status.objects.get(description='a')
                except Status.DoesNotExist:
                    active_status = Status.objects.create(description='a')
                
                Profile.objects.create(
                    user=instance,
                    status=active_status
                )
                print(f"⚠️  Perfil creado retroactivamente para: {instance.email}")