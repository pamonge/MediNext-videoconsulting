from rest_framework import serializers
from .models import Status, Benefit, User, Profile, Payment, MedicalHistory, MedicalFile, MedicalPlan, UserPlan, UploadFile

class StatusSerializer (serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class BenefitSerializer (serializers.ModelSerializer):
    class Meta:
        model = Benefit
        fields = '__all__'

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Para manejar correctamente la creación de usuarios con password
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

class ProfileSerializer (serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    user_dni = serializers.CharField(source='user.dni', read_only=True)
    
    class Meta:
        model = Profile
        fields = '__all__'

class PaymentSerializer (serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    user_dni = serializers.CharField(source='user.dni', read_only=True)
    status_description = serializers.CharField(source='status.description', read_only=True)
    
    class Meta:
        model = Payment
        fields = '__all__'
      
class MedicalHistorySerializer (serializers.ModelSerializer):
    patient_dni = serializers.CharField(source='patient.dni', read_only=True)
    doctor_email = serializers.EmailField(source='doctor.email', read_only=True, allow_null=True)
    status_description = serializers.CharField(source='status.description', read_only=True)
    
    class Meta:
        model = MedicalHistory
        fields = '__all__'

class MedicalFileSerializer (serializers.ModelSerializer):
    uploaded_by_email = serializers.EmailField(source='uploaded_by.email', read_only=True, allow_null=True)
    status_description = serializers.CharField(source='status.description', read_only=True)
    
    class Meta:
        model = MedicalFile
        fields = '__all__'

class MedicalPlanSerializer (serializers.ModelSerializer):
    benefits_details = serializers.StringRelatedField(many=True, read_only=True)
    status_description = serializers.CharField(source='status.description', read_only=True)
    
    class Meta:
        model = MedicalPlan
        fields = '__all__'

class UserPlanSerializer (serializers.ModelSerializer):
    user_dni = serializers.CharField(source='user.dni', read_only=True)
    plan_name = serializers.CharField(source='plan.plan_name', read_only=True)
    status_description = serializers.CharField(source='status.description', read_only=True)
    
    class Meta:
        model = UserPlan
        fields = '__all__'

class UploadFileSerializer (serializers.ModelSerializer):
    user_dni = serializers.CharField(source='user.dni', read_only=True)
    reviewed_by_email = serializers.EmailField(source='reviewed_by.email', read_only=True, allow_null=True)
    status_description = serializers.CharField(source='status.description', read_only=True)
    
    class Meta:
        model = UploadFile
        fields = '__all__'