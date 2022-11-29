from django.db import models
from base.models import BaseModel,ConditionChoices,HandOverTypeChoices
from django.contrib.auth import get_user_model
User = get_user_model()

class Category(BaseModel):
    """
    Electronics, Stationary, Furniture, Accessories, Computer
    """
    name=models.CharField(max_length=100)
    company=models.ForeignKey('company.Company', on_delete=models.RESTRICT)
    class Meta:
        ordering = ['-created_at']
        db_table = 'categories'
        indexes = [
            models.Index(fields=['-created_at']),
        ]

    def __str__(self):
        return self.name

class Asset(BaseModel):

    name=models.CharField(max_length=100)
    category=models.ForeignKey('asset.Category', on_delete=models.RESTRICT)
    condition=models.CharField(max_length=20,choices=ConditionChoices.choices)
    note=models.TextField()

    class Meta:
        ordering = ['-created_at']
        db_table = 'assets'
        indexes = [
            models.Index(fields=['-created_at']),
        ]

    def __str__(self):
        return self.name

class HandOverOrReturn(BaseModel):
    asset=models.ForeignKey('asset.Asset', on_delete=models.RESTRICT)
    condition=models.CharField(max_length=20,choices=ConditionChoices.choices)
    employee=models.ForeignKey('employee.Employee', on_delete=models.RESTRICT)
    admin=models.ForeignKey(User, on_delete=models.RESTRICT,related_name='admin')
    handover_or_return=models.CharField(max_length=20,choices=HandOverTypeChoices.choices)
    handover_date=models.DateField()
    
    class Meta:
        ordering = ['-created_at']
        db_table = 'handovers'
        indexes = [
            models.Index(fields=['-created_at']),
        ]

    def __str__(self):
        return self.asset.name


