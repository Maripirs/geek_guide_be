from django.contrib import admin

# Register your models here.
from . models import *

admin.site.register(Game)
admin.site.register(Section)


# admin.site.register(Image)
admin.site.register(Content)
admin.site.register(ExtendedContent)
