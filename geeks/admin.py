# from django.contrib import admin
from django.contrib import admin 
from django.forms import TextInput, Textarea
# Register your models here.
from . models import *

# admin.site.register(Game)
# admin.site.register(Section)


# admin.site.register(Image)
# admin.site.register(Content)



class ExtendedInline(admin.StackedInline):
    model = ExtendedContent
    extra=0
    # sortable_field_name = "order"
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':70})},
    }

class ContentInline(admin.StackedInline):
    fields: ("name", "text", "type", "image","direction", "order") 
    model = Content
    extra=0
    # sortable_field_name = "order"
    inlines = [ExtendedInline]
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':70})},
    }


class SectionInline(admin.StackedInline):
    model = Section
    extra=0
    # sortable_field_name = "game"
    inlines = [ContentInline]

class ContentAdmin(admin.ModelAdmin):
    inlines = [ExtendedInline]
    list_filter = ('section',)
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':70})},
    }

class SectionAdmin(admin.ModelAdmin):
    inlines = [ContentInline]
    list_filter = ('game',)
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':70})},
    }

class GameAdmin(admin.ModelAdmin):
    inlines = [SectionInline]








admin.site.register(Game, GameAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Content, ContentAdmin)
