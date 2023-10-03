from django.contrib import admin
from .models import airport,Flight,passenger
# Register your models here.


admin.site.register(airport)
admin.site.register(Flight)
admin.site.register(passenger)