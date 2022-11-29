from django.db import models
from base.models import BaseModel
# Create your models here.
class Company(BaseModel):
    name=models.CharField(max_length=50)

    class Meta:
        ordering = ['-created_at']
        db_table = 'companies'
        indexes = [
            models.Index(fields=['-created_at']),
        ]

    def __str__(self):
        return self.name