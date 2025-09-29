from django.contrib import admin
from .models import Status, Benefit, User, Profile, Payment, MedicalHistory, MedicalFile, MedicalPlan, UserPlan, UploadFile

admin.site.register(Status)
admin.site.register(Benefit)
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Payment)
admin.site.register(MedicalHistory)
admin.site.register(MedicalFile)
admin.site.register(MedicalPlan)
admin.site.register(UserPlan)
admin.site.register(UploadFile)