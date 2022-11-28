from django.contrib import admin

from .models import Armazones, Cristales, Lentes_Sol, Avatar

# Register your models here.

admin.site.register(Armazones)
admin.site.register(Cristales)
admin.site.register(Lentes_Sol)
admin.site.register(Avatar)
