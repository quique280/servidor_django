from django.contrib import admin

# Register your models here.
from .models import Prueba
admin.site.register(Prueba)

from .models import Inferencia
admin.site.register(Inferencia)

from .models import Deduccion
admin.site.register(Deduccion)