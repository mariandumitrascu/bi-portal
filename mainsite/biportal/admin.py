import os, time, uuid
from urllib.parse import quote as urlquote

from django.contrib import admin
from django.utils.html import mark_safe
from django.urls import reverse
from django.utils.html import format_html
from django import forms
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.files import File
from django.utils.translation import gettext as _, ngettext
from django.conf import settings

from sorl.thumbnail.admin import AdminImageMixin

from .models import Presentation, Bipage, Snippet

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

###########################################################################################################

class PresentatioAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PresentatioAdminForm, self).__init__(*args, **kwargs)

        # self.fields['embedded'].label = 'Embedded report'
        self.fields['description'].widget = forms.Textarea(attrs={'cols': '40', 'rows': '10'})

    class Meta:
        model = Presentation
        fields = '__all__'

@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):

    form = PresentatioAdminForm

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

    actions = ['render_all_snippets_in_selected_presentations']

    def render_all_snippets_in_selected_presentations(self, request, queryset):
        pass
        # queryset.update(status='p')

    def render_change_form(self, request, context, *args, **kwargs):
        """We need to update the context to show the button."""

        # add a new key to the context
        context.update({'show_render_all_report_snippets': True})
        return super().render_change_form(request, context, *args, **kwargs)

    def response_post_save_change(self, request, obj):
        """This method is called by `self.changeform_view()` when the form
        was submitted successfully and should return an HttpResponse.
        """
        # Check that you clicked the button `_render_snippets`
        if '_render_snippets' in request.POST:

            # Create a copy of your object
            # Assuming you have a method `create_from_existing()` in your manager
            # new_obj = self.model.objects.create_from_existing(obj)
            # do something with obj

            # Get its admin url
            opts = self.model._meta
            info = self.admin_site, opts.app_label, opts.model_name
            route = '{}:{}_{}_change'.format(*info)

            # post_url = reverse(route, args=(new_obj.pk,))
            # post_url = reverse(route, args=(obj.pk,))
            post_url = "/admin/biportal/presentation/{}/change/".format(obj.pk)

            # And redirect
            return HttpResponseRedirect(post_url)

        else:

            # Otherwise, use default behavior
            return super().response_post_save_change(request, obj)



###################################################################################################
###################################################################################################
###################################################################################################


class SnippetAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SnippetAdminForm, self).__init__(*args, **kwargs)

        self.fields['embedded'].label = 'Embedded report code'
        self.fields['embedded'].widget = forms.Textarea(attrs={'cols': '80', 'rows': '3'})

        # self.fields['report_rendered_preview'].label = 'Rendered report'
    class Meta:
        model = Snippet
        fields = '__all__'

##################################################################################################
@admin.register(Snippet)
# class SnippetAdmin(AdminImageMixin, admin.ModelAdmin):
class SnippetAdmin(admin.ModelAdmin):

    form = SnippetAdminForm

    change_form_template = 'admin/change_form.html'

    ordering = ('created_at',)

    readonly_fields = ['created_at','report_rendered_preview', 'report_snippet_preview', 'render_button']

    list_filter = ['tags', 'created_by', 'created_at']

    fieldsets = [
        (
            'Basic Information',
            {
                'fields': ['name', 'embedded', 'render_button']
            }
        ),
        (
            'Snippet Image',
            {
                'fields':
                [
                    ('report_rendered_preview', 'image_rendered'),
                    # ('image_cropped', 'image_cropped_full_preview')
                    # 'image_cropped',
                    # 'image_cropped_full_preview'
                    ('report_snippet_preview', 'image_cropped',)
                ]
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

    search_fields = ['name', 'created_at']

    list_per_page = 5

    # reference:
    # https://ilovedjango.com/django/admin/how-to-show-image-from-imagefield-in-django-admin-page/
    def report_rendered_preview(self, obj):
        return mark_safe("<img src={url} width={width} height={height} />".format(
            url = obj.image_rendered.url,
            width=obj.image_rendered.width,
            height=obj.image_rendered.height
            ))

    def report_snippet_preview(self, obj):
        return mark_safe("<img src={url} width={width} height={height} />".format(
            url = obj.image_cropped.url,
            width=obj.image_cropped.width,
            height=obj.image_cropped.height
            ))
    def image_cropped_preview(self, obj):
        return mark_safe("<img src={url} width=220 />".format(
            url = obj.image_cropped.url,
            ))

    def image_rendered_preview(self, obj):
        return mark_safe("<img src={url} width={width} height={height} />".format(
            url = obj.image_rendered.url,
            width=obj.image_rendered.width,
            height=obj.image_rendered.height
            ))

    # method that acts like a field
    # this adds a button to render the embedded report as an image
    # MD: moved to model
    # def render_button(self, obj):
    #     return mark_safe('<input type="submit" value="Render report" name="_render_report">')




    ##########################################################################################
    # default created_by user with curent user
    # overwrite get_changeform_initial_data
    def get_changeform_initial_data(self, request):
        get_data = super(SnippetAdmin, self).get_changeform_initial_data(request)
        get_data['created_by'] = request.user.pk
        return get_data



    # this is adding an extra action to the list of actions in the list form
    actions = ['render_all_reports_in_selected_snippets']

    # code behind the extra action
    def render_all_reports_in_selected_snippets(self, request, queryset):
        pass
        # queryset.update(status='p')

    def response_change(self, request, obj):

        return super().response_change(request, obj)

    # one way to modify data when pressing a custom action
    def response_post_save_change(self, request, obj):
        """This method is called by `self.changeform_view()` when the form
        was submitted successfully and should return an HttpResponse.
        """
        # Check that you clicked the button `_render_snippets`
        if '_render_report' in request.POST:

            # obj is the model data
            # do something with obj



            # reference: saving image file to django ImageField
            # https://stackoverflow.com/questions/1308386/programmatically-saving-image-to-django-imagefield
            # https://stackoverflow.com/questions/13393191/programmatically-add-file-to-django-imagefield

            # MEDIA_ROOT
            # obj.image_rendered = '/Users/marian.dumitrascu/Dropbox/Work/Current/python-cms/bi-portal/mainsite/media/image_rendered/tableau-scrap-screenshot.png'
            # obj.save()

            # obj.image_rendered = 'image_rendered/tableau-scrap-screenshot.png'
            # obj.save()
            obj.embedded = os.environ
            obj.save()

            opts = self.model._meta
            preserved_filters = self.get_preserved_filters(request)

            msg = _('The report was rendered successsfuly')
            self.message_user(request, msg, messages.SUCCESS)


            # post_url = reverse(route, args=(new_obj.pk,))
            # post_url = reverse(route, args=(obj.pk,))
            post_url = "/admin/biportal/snippet/{}/change/".format(obj.pk)

            # And redirect
            # return super().response_post_save_change(request, obj)
            return HttpResponseRedirect(post_url)

        else:

            # Otherwise, use default behavior
            return super().response_post_save_change(request, obj)


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

            ###########################
            # instance.name = 'test changed snippet 1001'

            instance.save()
            form.save_m2m()
            return instance



# admin.site.register(Presentation)
# admin.site.register(Snippet)
