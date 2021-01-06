from django.contrib import admin

from .models import Presentation, Bipage, Snippet, MasterLayout

# Register your models here.


class BipageInline(admin.StackedInline):
    model = Bipage
    extra = 3

@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):

    # fields = ['name', 'description', 'active', 'created_by', 'tags']

    fieldsets = [
        (
            'Basic Information',
            {
                'fields': ['name', 'description','created_by', 'active']
            }
        ),

        (
            'Metadata',
            {
                'fields': ['tags']
            }
        ),
    ]


    search_fields = ['name', 'description',]

    list_filter = ['tags', 'created_by', 'active']

    list_display = ['name', 'created_by', 'created_at','updated_at', 'active']

    list_editable = ['active']

    inlines = [BipageInline]

    list_per_page = 5

# admin.site.register(Presentation)
admin.site.register(Snippet)
# admin.site.register(MasterLayout)