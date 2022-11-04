from django.contrib import admin

from .models import Armazones, Cristales, Lentes_Sol

# Register your models here.

admin.site.register(Armazones)
admin.site.register(Cristales)
admin.site.register(Lentes_Sol)
