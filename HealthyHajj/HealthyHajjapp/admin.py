from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import *


# Register your models here.
admin.site.register(Doctor)
admin.site.register(HajjParticipant)
admin.site.register(Delegation)
admin.site.register(MedicalHistory)
admin.site.register(Ilness)
