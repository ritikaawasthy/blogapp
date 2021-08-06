from django.contrib import admin
from .models import Blog, ExtendedUser
# Register your models here.
admin.site.register(ExtendedUser)
admin.site.register(Blog)
