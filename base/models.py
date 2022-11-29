from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class BaseModel(models.Model):
    class StatusChoices(models.TextChoices):
        ACTIVE = 'active', _('active')
        INACTIVE = 'inactive', _('inactive')
        ARCHIVED = 'archived', _('archived')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='created_%(class)ss')
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE,  related_name='updated_%(class)ss', null=True, blank=True)

    class Meta:
        abstract = True
        