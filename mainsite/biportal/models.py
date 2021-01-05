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

###########################################################################################################
class Snippet(models.Model):
    name = models.CharField(max_length=50, blank=True)
    file = models.ImageField()
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    tags = TaggableManager()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'snippet'
        verbose_name_plural = 'snippets'


###########################################################################################################
class MasterLayout(models.Model):
    name = models.CharField(
        max_length=200,
        blank=False)

    file = models.FileField()

    created_by = models.ForeignKey(
        User,
        # related_name='creator',
        null = True,
        on_delete=models.CASCADE
        )

    # updated_by = models.ForeignKey(
    #     User,
    #     # related_name='updater',
    #     null = True,
    #     on_delete=models.CASCADE
    #     )

    created_at = models.DateTimeField(
        auto_now=True,
        # default=timezone.now()
        )

    updated_at = models.DateTimeField(
        auto_now_add=True,
        # default=timezone.now()
        )
