from rest_framework import permissions

# Permisos personalizados para Usuario:
#  - Listar y ver: todos
#  - Crear y modificar: admins y staff
#  - Eliminar: solo admin
class UserPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        
        if request.method in ['POST', 'PUT', 'PATCH']:
            return request.user and request.user.is_authenticated and request.user.user_type in ['s', 'a']

        if request.method == 'DELETE':
            return request.user and request.user.is_authenticated and request.user.user_type == 'a'
        
        return False

# Modo seguro, lectura a todos, escritura solo a admin
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user and request.user.is_authenticated and request.user.user_type == 'a'      

# Permiso para dueño o admin, sino solo lectura
#  - Lectura: usuario autenticado
#  - Escritura: Dueño y admin
#  - Creacion: automatico al crear el usuario
#  - Eliminación: solo admin
class IsOwnerAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated

        if request.method in ['PUT', 'PATCH']:
            return obj.user == request.user or request.user.user_type == 'a'

        if request.method == 'DELETE':
            return request.user.user_type == 'a'
        
        return False

# Sólo el dueño o admin pueden ingresar
class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.user_type == 'a'

class CanViewProfile(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        
        if obj.user == request.user:
            return True
        
        if request.user.user_type == 'a' or request.user.user_type == 'd':
            return True

        return False

class PaymentPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user and request.user.is_authenticated
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        return request.user and request.user.is_authenticated and request.user.user_type in ['a', 's']
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return obj.user == request.user or request.user.user_type in ['a', 's']
        return request.user.user_type in ['a', 's']