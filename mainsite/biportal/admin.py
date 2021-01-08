from django.contrib import admin
from .models import Presentation, Bipage, Snippet
from django.utils.html import mark_safe
from django.urls import reverse
from django.utils.html import format_html

from sorl.thumbnail.admin import AdminImageMixin

# references:
# for sorl.thumbnail: https://sorl-thumbnail.readthedocs.io/en/latest/examples.html



# class BipageInline(admin.StackedInline):
class BipageInline(admin.TabularInline):
    model = Bipage
    show_change_link = True
    fields = ['image_slidepage_preview', 'name', 'ppt_page_layout', 'last_updated', 'edit']
    readonly_fields = ['last_updated', 'image_slidepage_preview', 'edit']
    list_display = ['image_slidepage_preview', 'name', 'ppt_page_layout', 'last_updated']
    can_delete = True

    # prepopulated_fields = {"name": ("",)}
    extra = 1

    list_per_page = 5

    per_page = 5

    def image_slidepage_preview(self, obj):
        return mark_safe("<img src='/static/biportal/img/SlidePage.png' />")

    def edit(self, instance):
        # url = reverse('admin:bipage'
        # return format_html(u'<a href="{}">Edit</a>', url)
        # # … or if you want to include other fields:
        # return format_html(u'<a href="{}">Edit: {}</a>', '/admin/bipage', instance.title)
        return format_html(u'<a href="{}">Edit</a>', '/admin/bipage')

@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):

    # fields = ['name', 'description', 'active', 'created_by', 'tags']

    readonly_fields = ['created_at']

    fieldsets = [
        (
            'Basic Information',
            {
                'fields': ['name', 'description', 'ppt_master_file', 'active']
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
# class SnippetAdmin(AdminImageMixin, admin.ModelAdmin):
class SnippetAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'image_cropped_preview']

    list_filter = ['tags', 'created_by', 'created_at']

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
                'fields': [
                    'image_rendered',
                    ('image_cropped', 'image_cropped_preview')]
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

    list_display = ['image_cropped_preview', 'name', 'created_by', 'created_at','updated_at']

    search_fields = ['name', 'created_at', 'tags']

    list_per_page = 3

    # reference:
    # https://ilovedjango.com/django/admin/how-to-show-image-from-imagefield-in-django-admin-page/
    def image_cropped_preview(self, obj):
        return mark_safe("<img src={url} width={width} height={height} />".format(
            url = obj.image_cropped.url,
            width=obj.image_cropped.width,
            height=obj.image_cropped.height
            ))

    def image_rendered_preview(self, obj):
        return mark_safe("<img src={url} width={width} height={height} />".format(
            url = obj.image_rendered.url,
            width=obj.image_rendered.width,
            height=obj.image_rendered.height
            ))


    # default created_by user with curent user
    # overwrite get_changeform_initial_data
    def get_changeform_initial_data(self, request):
        get_data = super(SnippetAdmin, self).get_changeform_initial_data(request)
        get_data['created_by'] = request.user.pk
        return get_data


    # reference:
    # https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/
    # https://stackoverflow.com/questions/4670783/make-the-user-in-a-model-default-to-the-current-user
    # every time you save a form using commit=False, Django adds a save_m2m()
    # method to your ModelForm subclass. After you’ve manually saved the instance
    # produced by the form, you can invoke save_m2m()
    # to save the many-to-many form data. For example:
    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change or not instance.created_by:
            instance.created_by = user
        instance.updated_by = user
        instance.save()
        form.save_m2m()
        return instance

# admin.site.register(Presentation)
# admin.site.register(Snippet)
