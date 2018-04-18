from django.contrib import admin
from clock.models import shiftTime
# Register your models here.

class ShiftTimeAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}

'''class ClockOutAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}
'''
admin.site.register(shiftTime)
