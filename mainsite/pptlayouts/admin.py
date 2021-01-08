from django.contrib import admin
from django.utils.html import mark_safe
from django.urls import reverse
from django.utils.html import format_html
from django import forms

from sorl.thumbnail.admin import AdminImageMixin
from sorl.thumbnail import get_thumbnail
from sorl.thumbnail import ImageField



from .models import PPTMasterLayout, PPTPageLayout





class PPTPageLayoutInline(admin.TabularInline):
    model = PPTPageLayout

    fields = ['image_thumbnail_preview', 'name', 'web_page_layout', 'edit']

    readonly_fields = ['image_thumbnail_preview', 'edit']

    list_display = ['image_slidepage_preview', 'name', 'web_page_layout']

    extra = 1

    def image_thumbnail_preview(self, obj):
        # return mark_safe("<img src='{}' />".format(self.image_thumbnail.url))
        # return mark_safe("<img src='/static/biportal/slides/layout1.png' />")
        # return mark_safe("<img src='/static/biportal/slides/layout{}.png' />".format(obj.pk))
        return mark_safe("<img src={} />".format(
            obj.image_thumbnail.url,
            # self.image_thumbnail.width,
            # self.image_thumbnail.height,
        ))

    def edit(self, instance):
        # url = reverse('admin:bipage'
        # return format_html(u'<a href="{}">Edit</a>', url)
        # # … or if you want to include other fields:
        # return format_html(u'<a href="{}">Edit: {}</a>', '/admin/bipage', instance.title)
        return format_html(u'<a href="{}">Edit</a>', '/admin/pptlayouts/pptpagelayout/1')




class MasterLayoutAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MasterLayoutAdminForm, self).__init__(*args, **kwargs)

        # self.fields['embedded'].label = 'Embedded report'
        self.fields['description'].widget = forms.Textarea(attrs={'cols': '40', 'rows': '5'})

    class Meta:
        model = PPTMasterLayout
        fields = '__all__'

@admin.register(PPTMasterLayout)
class PPTMasterLayoutAdmin(admin.ModelAdmin):

    form = MasterLayoutAdminForm

    readonly_fields = ['created_at']

    fieldsets = [
        (
            'Basic Information',
            {
                'fields': ['name', 'description', 'ppt_master_file', ]
            }
        ),

        (
            'Metadata',
            {
                'fields': ['created_by', 'created_at']
            }
        ),
    ]

    search_fields = ['name', 'description',]

    list_filter = ['created_by']

    list_display = ['name', 'created_by', 'created_at','updated_at']

    # list_editable = ['active']

    inlines = [PPTPageLayoutInline]

    # save_as = True

    list_per_page = 5

########################################################################################
########################################################################################
########################################################################################



# admin.site.register(PPTPageLayout)