from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .permissions import IsAdminOrReadOnly, IsOwnerAdminOrReadOnly, PaymentPermissions
from .models import Status, Benefit, User, Profile, Payment, MedicalHistory, MedicalFile, MedicalPlan, UserPlan, UploadFile
from .serializers import StatusSerializer, BenefitSerializer, UserSerializer, ProfileSerializer, PaymentSerializer, MedicalHistorySerializer, MedicalFileSerializer, MedicalPlanSerializer, UserPlanSerializer, UploadFileSerializer

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAdminOrReadOnly]

class BenefitViewSet(viewsets.ModelViewSet):
    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerAdminOrReadOnly]

    def get_queryset(self):
        # Los usuarios solo ven su perfil, los admnistradores ven todos
        user = self.request.user

        if user.is_authenticated:
            if user.user_type in ['a', 'd']: 
                return Profile.objects.select_related('user')
            return Profile.objects.filter(user=user)
        return Profile.objects.none()
    
    @action(detail=False, methods=['get'])
    def me(self, request):
        # Endpoint para obtener el usuario actual
        try:
            profile = request.user.profile
            serializer = self.get_serializer(profile)
            return Response(serializer.data)
        except Profile.DoesNotExist:
            return Response(
                {'error': 'Perfil no encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )
        except AttributeError:
            return Response(
                {'error': 'Usuario no autenticado'},
                status=status.HTTP_401_UNAUTHORIZED
            )

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.select_related('user', 'status').all()
    serializer_class = PaymentSerializer
    permission_classes = [PaymentPermissions]
    
    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Payment.objects.none()
        if user.user_type in ['a', 's']:
            return Payment.objects.select_related('user', 'status')
        return Payment.objects.filter(user=user).select_related('status')

class MedicalHistoryViewSet(viewsets.ModelViewSet):
    queryset = MedicalHistory.objects.select_related('patient', 'doctor', 'status').all()
    serializer_class = MedicalHistorySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'a':  # Admin ve todo
            return MedicalHistory.objects.all()
        elif user.user_type == 'd':  # Doctor ve sus historias
            return MedicalHistory.objects.filter(doctor=user)
        else:  # Paciente ve sus historias
            return MedicalHistory.objects.filter(patient=user)

class MedicalFileViewSet(viewsets.ModelViewSet):
    queryset = MedicalFile.objects.select_related('medical_history', 'uploaded_by', 'status').all()
    serializer_class = MedicalFileSerializer
    permission_classes = [permissions.IsAuthenticated]

class MedicalPlanViewSet(viewsets.ModelViewSet):
    queryset = MedicalPlan.objects.prefetch_related('benefits').all()
    serializer_class = MedicalPlanSerializer
    permission_classes = [IsAdminOrReadOnly]

class UserPlanViewSet(viewsets.ModelViewSet):
    queryset = UserPlan.objects.select_related('user', 'plan', 'status').all()
    serializer_class = UserPlanSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.user_type in ['a', 's']:
            return UserPlan.objects.all()
        return UserPlan.objects.filter(user=user)

class UploadFileViewSet(viewsets.ModelViewSet):
    queryset = UploadFile.objects.select_related('user', 'reviewed_by', 'status').all()
    serializer_class = UploadFileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.user_type in ['a', 's']:
            return UploadFile.objects.all()
        return UploadFile.objects.filter(user=user)