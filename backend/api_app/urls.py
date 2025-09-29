from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'status', views.StatusViewSet)
router.register(r'benefits', views.BenefitViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'profiles', views.ProfileViewSet)
router.register(r'payments', views.PaymentViewSet)
router.register(r'medical-histories', views.MedicalHistoryViewSet)
router.register(r'medical-files', views.MedicalFileViewSet)
router.register(r'medical-plans', views.MedicalPlanViewSet)
router.register(r'user-plans', views.UserPlanViewSet)
router.register(r'upload-files', views.UploadFileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]