from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.core.validators import FileExtensionValidator
import uuid
import os

# FUNCION -------------------------------------------------------------------------------
# renombrar los archivos subidos
def user_directory_path(instance, filename):
    # El archivo se va a subir a: MEDIA_ROOT/user_<id>/<nombre_archivo>
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    if hasattr(instance, 'user'):
        return f'user_{instance.user.id}/{filename}'
    elif hasattr(instance, 'dni'):
        return f'user_{instance.dni.id}/{filename}'
    else:
        return f'files/{filename}'

# MODELOS --------------------------------------------------------------------------------

# Modelo de Status (primero porque otros modelos lo referencian)
class Status(models.Model):
    STATUS_CHOICES = (
        ('a', 'Activo'),
        ('d', 'Inactivo'),
        ('p', 'Pendiente'),
        ('s', 'Suspendido'),
        ('r', 'Revisión'),
        ('c', 'Cancelado'),
        ('e', 'En proceso'),
        ('f', 'Finalizado'),
        ('v', 'Vencido'),
        ('n', 'No aplica'),
        ('o', 'Otro'),
        ('b', 'Baja'),
        ('m', 'Mora'),
        ('t', 'Temporal'),
        ('u', 'Urgente'),
        ('i', 'Incompleto'),
        ('l', 'Lista'),
        ('q', 'En cola'),
    )

    description = models.CharField(max_length=1, choices=STATUS_CHOICES)

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'

    def __str__(self):
        return f'{self.get_description_display()}'

# Modelo de Beneficios
class Benefit(models.Model):
    detail = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Beneficio'
        verbose_name_plural = 'Beneficios'

    def __str__(self):
        return f'{self.detail}'

# Modelo de Usuario personalizado
class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('c', 'Client'),
        ('d', 'Doctor'),
        ('a', 'Admin'),
        ('s', 'Staff'),
    )

    dni = models.CharField(max_length=8, unique=True)
    email = models.EmailField(unique=True)  
    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES, default='c')
    is_verified = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    # Usa el correo como username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'dni'] 

    # campos groups y user_permissions con related_name personalizado
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='El grupo al cual pertenece un usuario. Un usuario obtendrá todos los permisos de cada grupo al que pertenezca.',
        related_name="custom_user_groups",
        related_query_name="custom_user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Permisos especificos para un usuario en particular',
        related_name="custom_user_permissions",
        related_query_name="custom_user",
    )

    class Meta:
        ordering = ['dni'] 
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{self.dni} ({self.get_user_type_display()})'

# Modelo de Profile
class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
        ('N', 'Prefiero no decir'),
    )

    CITY_CHOICES = (
       ('mu', 'Maipu'),
       ('sr', 'San Rafael'),
       ('cp', 'Capital'),
       ('gu', 'Guaymallen'),
       ('gc', 'Godoy Cruz'),
       ('sm', 'San Martin'),
       ('lh', 'Las Heras'),
       ('tn', 'Tunuyan'),
       ('ri', 'Rivadavia'),
       ('ju', 'Junin'),
       ('ga', 'Gral Alvear'),
       ('sc', 'San Carlos'),
       ('to', 'Tupungato'),
       ('la', 'Lavalle'),
       ('me', 'Malargue'),
       ('lp', 'La Paz'),
       ('sa', 'Santa Rosa'), 
    )  

    MARITAL_STATUS_CHOICES = (
        ('s', 'Soltero'),
        ('m', 'Casado'),
        ('w', 'Viudo'),
        ('d', 'Divorciado'),  
        ('c', 'Concubinato'), 
        ('o', 'Otro'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True) 
    birth_date = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    marital_status = models.CharField(max_length=1, choices=MARITAL_STATUS_CHOICES, blank=True, null=True)  
    occupation = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=2, choices=CITY_CHOICES, blank=True, null=True)  
    zip_code = models.CharField(max_length=4, blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=100, blank=True, null=True)  
    emergency_contact_phone = models.CharField(max_length=11, blank=True, null=True)  
    avatar = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True, related_name='profiles') 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['user__dni']  # Corregido
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
    
    def __str__(self):
        return f'Perfil de {self.user.dni} - {self.status}'

# Modelo de Payment
class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = (
        ('cash', 'Efectivo'),
        ('card', 'Tarjeta'),
        ('transfer', 'Transferencia'),
        ('other', 'Otro'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments') 
    payment_date = models.DateTimeField() 
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True, related_name='payments')  
    transaction_id = models.CharField(max_length=100, unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-payment_date']
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'

    def __str__(self):
        return f'{self.id} - {self.user.dni} - {self.status}'

# Modelo de Historia Médica
class MedicalHistory(models.Model):  
    HISTORY_TYPE_CHOICES = (
        ('consult', 'Consulta'),
        ('diagnosis', 'Diagnóstico'),
        ('treatment', 'Tratamiento'),
        ('surgery', 'Cirugía'),
        ('control', 'Control'),
        ('emergency', 'Emergencia'),
    )

    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='medical_histories_as_patient', limit_choices_to={'user_type': 'c'})
    doctor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='medical_histories_as_doctor', limit_choices_to={'user_type': 'd'})
    history_type = models.CharField(max_length=20, choices=HISTORY_TYPE_CHOICES, default='consult')
    title = models.CharField(max_length=200)
    description = models.TextField()
    diagnosis = models.TextField(blank=True, null=True)
    treatment = models.TextField(blank=True, null=True)
    prescriptions = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    consultation_date = models.DateTimeField()
    next_control_date = models.DateTimeField(blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True, related_name='medical_histories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-consultation_date']
        verbose_name = 'Historia Médica'
        verbose_name_plural = 'Historias Médicas'

    def __str__(self):
        return f'{self.id} - {self.patient.dni} - {self.history_type}'

# Modelo para archivos médicos (estudios, imágenes, etc.)
class MedicalFile(models.Model):
    FILE_TYPE_CHOICES = (
        ('lab', 'Laboratorio'),
        ('image', 'Imagen'),
        ('scan', 'Escáner'),
        ('xray', 'Radiografía'),
        ('ultrasound', 'Ultrasonido'),
        ('prescription', 'Receta'),
        ('report', 'Reporte'),
        ('other', 'Otro'),
    )

    medical_history = models.ForeignKey(MedicalHistory, on_delete=models.CASCADE, related_name='files')
    file_type = models.CharField(max_length=20, choices=FILE_TYPE_CHOICES)
    file = models.FileField(
        upload_to=user_directory_path,
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png', 'doc', 'docx', 'txt'])]
    )
    description = models.TextField(blank=True, null=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True, related_name='medical_files')

    class Meta:
        verbose_name = 'Archivo Médico'
        verbose_name_plural = 'Archivos Médicos'

    def __str__(self):
        return f'{self.id} - {self.medical_history.id} - {self.file_type}'

# Modelo del Plan Médico
class MedicalPlan(models.Model):
    plan_id = models.CharField(max_length=25, unique=True)  
    plan_name = models.CharField(max_length=100)
    plan_price = models.DecimalField(max_digits=10, decimal_places=2)
    plan_detail = models.TextField()
    benefits = models.ManyToManyField(Benefit, related_name='plans')
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True, related_name='medical_plans')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Plan Médico'
        verbose_name_plural = 'Planes Médicos' 

    def __str__(self):
        return f'{self.plan_id} - {self.plan_name}'

# Modelo de Plan por Usuario
class UserPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_plans')  
    plan = models.ForeignKey(MedicalPlan, on_delete=models.CASCADE, related_name='user_plans')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_plans')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Plan Usuario'
        verbose_name_plural = 'Planes Usuarios'

    def __str__(self):
        return f'{self.id} - {self.user.dni} - {self.plan.plan_id}'

# Modelo para subir archivos para autorizar
class UploadFile(models.Model):
    FILE_CATEGORY_CHOICES = (
        ('authorization', 'Autorización'),
        ('document', 'Documento'),
        ('id', 'Identificación'),
        ('insurance', 'Seguro'),
        ('other', 'Otro'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_files') 
    category = models.CharField(max_length=20, choices=FILE_CATEGORY_CHOICES)
    description = models.TextField()
    file = models.FileField(
        upload_to=user_directory_path,
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png', 'doc', 'docx'])]
    )
    upload_date = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True, related_name='uploaded_files')
    reviewed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviewed_files')
    review_date = models.DateTimeField(blank=True, null=True)
    review_notes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Archivo'
        verbose_name_plural = 'Archivos'

    def __str__(self):
        return f'{self.id} - {self.user.dni} - {self.category}'