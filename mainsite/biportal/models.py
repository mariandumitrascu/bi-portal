import math

from django.contrib.auth.models import User
from django.db import models
from django.utils.html import mark_safe
from django.utils.text import Truncator
from taggit.managers import TaggableManager
from django.utils import timezone

# Create your models here.



###########################################################################################################
class Presentation(models.Model):
    name = models.CharField(
        max_length=30,
        # unique=True
        )

    description = models.CharField(
        max_length=1000,
        default='',
        blank=True
        )

    # pages = models.PositiveIntegerField(
    #     editable=False
    #     )

    created_by = models.ForeignKey(
        User,
        related_name='creator',
        null = True,
        on_delete=models.CASCADE
        )

    updated_by = models.ForeignKey(
        User,
        related_name='updater',
        null = True,
        on_delete=models.CASCADE
        )

    created_at = models.DateTimeField(
        editable=False,
        auto_now=True,
        # default=timezone.now()
        )

    updated_at = models.DateTimeField(
        auto_now_add=True,
        # default=timezone.now()
        )

    active = models.BooleanField(
        default=True
        )

    tags = TaggableManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Presentation'
        verbose_name_plural = 'Presentations'
        ordering = ["-created_at"]

###########################################################################################################
class Bipage(models.Model):
    name = models.CharField(
        max_length=30,
        )

    presentation = models.ForeignKey(
        Presentation,
        related_name='presentations',
        on_delete=models.CASCADE
        )

    last_updated = models.DateTimeField(
        auto_now_add=True
        )

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'BI Page'
        verbose_name_plural = 'BI Pages'

###########################################################################################################
class Snippet(models.Model):
    name = models.CharField(
        max_length=50,
        blank=True
        )

    # embedded = models.TextField(
    embedded = models.URLField(
        max_length=2000,
        blank=True
        )

    # file will be uploaded to MEDIA_ROOT/image_rendered
    image_rendered = models.ImageField(
        upload_to='image_rendered/',
        verbose_name='Rendered Report',
        null = True
        )

    image_cropped = models.ImageField(
        upload_to='image_cropped/',
        verbose_name='Report Snippet',
        null = True
        )

    x = models.PositiveIntegerField(
        default=0
        )

    y = models.PositiveIntegerField(
        default=0
        )

    w = models.PositiveIntegerField(
        default=0
        )

    h = models.PositiveIntegerField(
        default=0
        )

    created_at = models.DateTimeField(
        editable=False,
        auto_now=True,
        )

    updated_at = models.DateTimeField(
        auto_now_add=True,
        )

    created_by = models.ForeignKey(
        User,
        related_name='snippet_creator',
        null = True,
        on_delete=models.CASCADE
        )

    updated_by = models.ForeignKey(
        User,
        related_name='snippet_updater',
        null = True,
        on_delete=models.CASCADE
        )

    # will be available as bipage.pages_set and snippet.bipages
    pages = models.ManyToManyField(Bipage)

    tags = TaggableManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'snippet'
        verbose_name_plural = 'snippets'


###########################################################################################################
