from django.contrib import admin
from celero.models import Athlete

class Athletes (admin.ModelAdmin):
    list_display = ('id', 'name', 'sex')
    


admin.site.register(Athlete, Athletes)

# Register your models here.
