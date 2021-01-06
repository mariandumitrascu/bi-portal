from django.db import models
from django.contrib.auth.models import User

# Create your models here.


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
