from django.db import models
from django.contrib.auth.models import User

from PIL import Image
from sorl.thumbnail import get_thumbnail
from sorl.thumbnail import ImageField


class PPTMasterLayout(models.Model):
    name = models.CharField(
        max_length=200,
        blank=False)

    description = models.CharField(
        max_length=1000,
        default='',
        blank=True
        )

    ppt_master_file = models.FileField(
        null = True,
        blank = True,
        upload_to='ppt_master_files/'
        )

    master_file = models.FileField(
        null = True,
        blank = True
        )

    created_by = models.ForeignKey(
        User,
        related_name='masterlayout_created_by',
        null = True,
        on_delete=models.CASCADE
        )

    updated_by = models.ForeignKey(
        User,
        related_name='masterlayout_updated_by',
        null = True,
        on_delete=models.CASCADE
        )

    created_at = models.DateTimeField(
        auto_now=True,
        # default=timezone.now()
        )

    updated_at = models.DateTimeField(
        auto_now_add=True,
        # default=timezone.now()
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Master PPT Layout'
        verbose_name_plural = 'Master PPT Layouts'
        ordering = ["-created_at"]


#########################################################################################
web_page_layout_choices = [
    ('header', 'Header Page'),
    ('content1', 'Content With 1 Placeholder'),
    ('content2', 'Content With 2 Columns'),
    ('content3', 'Content With 3 Columns'),
]
class PPTPageLayout(models.Model):

    name = models.CharField(
        max_length=30,
        )

    master_layout = models.ForeignKey(
        PPTMasterLayout,
        related_name='pagelayouts',
        on_delete=models.CASCADE
        )

    web_page_layout = models.CharField(
        max_length = 20,
        null = True,
        blank = True,
        choices = web_page_layout_choices,
        default = 'content1',
        verbose_name = 'Web Page Layout'
        )

    # using sorl.thumbnail.ImageField
    image_thumbnail = ImageField(
        upload_to='ppt_page_layouts/',
        verbose_name='Page Layout Thumbnail',
        null = True,
        blank = True
        )


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'PPT Page Layout'
        verbose_name_plural = 'PPT Page Layouts'
