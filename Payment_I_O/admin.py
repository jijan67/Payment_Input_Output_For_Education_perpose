from django.contrib import admin
from .models import Course, Batch, Department
# Register your models here.

admin.site.register(Course)
admin.site.register(Batch)
admin.site.register(Department)