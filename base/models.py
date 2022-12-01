from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='created_%(class)ss')
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE,  related_name='updated_%(class)ss', null=True, blank=True)

    class Meta:
        abstract = True

class ConditionChoices(models.TextChoices):
    INTAKE = 'intake', ('intake')
    USED_LIKE_NEW = 'used_like_new', ('used_like_new')
    USED='used',('used')
    DAMAGED_BUT_USEABLE='damage_but_useable',('damage_but_useable')

class HandOverTypeChoices(models.TextChoices):
    RETURN_TO_ADMIN = 'return_to_admin', ('return_to_admin')
    HANDOVER_TO_EMPLOYEE='handover_to_employee',('handover_to_employee')

class OwnerChoices(models.TextChoices):
    ADMIN = 'admin', ('admin')
    EMPLOYEE='employee',('employee')