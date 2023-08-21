from django.contrib import admin
from .models import register_user, login, question

# Register your models here.
admin.site.register(register_user)
admin.site.register(login)
admin.site.register(question)
