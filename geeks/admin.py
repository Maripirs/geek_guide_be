from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

# Register your models here.
from . models import *

admin.site.register(Game)
admin.site.register(Section)


class SectionAdmin(admin.ModelAdmin, DynamicArrayMixin):
    formfield_overrides = {
    }


admin.site.register(Legend)
