from django.contrib import admin
from .models import Presentation, Bipage, Snippet

# Register your models here.


# class BipageInline(admin.StackedInline):
class BipageInline(admin.TabularInline):
    model = Bipage
    show_change_link = True
    fields = ['name', 'last_updated']
    readonly_fields = ['last_updated']
    list_display = ['name', 'last_updated']

    # prepopulated_fields = {"name": ("",)}
    extra = 3

@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):

    # fields = ['name', 'description', 'active', 'created_by', 'tags']

    readonly_fields = ['created_at']

    fieldsets = [
        (
            'Basic Information',
            {
                'fields': ['name', 'description', 'active']
            }
        ),

        (
            'Metadata',
            {
                'fields': ['created_by', 'created_at', 'tags']
            }
        ),
    ]

    search_fields = ['name', 'description',]

    list_filter = ['tags', 'created_by', 'active']

    list_display = ['name', 'created_by', 'created_at','updated_at', 'active']

    list_editable = ['active']

    inlines = [BipageInline]

    save_as = True

    list_per_page = 5


###################################################################################################
###################################################################################################
###################################################################################################
@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at']

    fieldsets = [
        (
            'Basic Information',
            {
                'fields': ['name', 'embedded']
            }
        ),
        (
            'Snippet Image',
            {
                'fields': ['image_rendered', 'image_cropped']
            }
        ),
        (
            'Position and Dimensions',
            {
                'fields': [('x', 'y'), ('w', 'h')],
                # 'description': 'sfdsfd dsf sdf ds fds  fds  f'
            }
        ),

        (
            'Metadata',
            {
                'fields': ['created_by', 'created_at', 'tags']
            }
        ),
    ]

    list_display = ['name', 'created_by', 'created_at','updated_at']

    list_per_page = 5

# admin.site.register(Presentation)
# admin.site.register(Snippet)
