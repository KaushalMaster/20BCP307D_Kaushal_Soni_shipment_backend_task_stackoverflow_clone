from django.contrib import admin
from .models import register_user, login

# Register your models here.
admin.site.register(register_user)
admin.site.register(login)
