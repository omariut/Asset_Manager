from django.db import models
from base.models import BaseModel

# Create your models here.


class Employee(BaseModel):
    name = models.CharField(max_length=100)
    company = models.ForeignKey("company.Company", on_delete=models.RESTRICT)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=50)

    class Meta:
        unique_together = ["company", "employee_id"]
        ordering = ["-created_at"]
        db_table = "employees"
        indexes = [
            models.Index(fields=["-created_at"]),
        ]

    def __str__(self):
        return self.name
