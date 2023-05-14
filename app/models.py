from django.db import models

class brand_add(models.Model):
    brand_name = models.CharField(max_length=200) 
    datetime = models.DateField(auto_now_add=True)
    status = models.IntegerField(default=0, choices=[(0, 'Inactive'), (1, 'Active')])

    class Meta:
        db_table = "brands_mstr"

class supplier(models.Model):
    supplier_name = models.CharField(max_length=50)
    mobile_no = models.IntegerField()
    address = models.CharField(max_length=100)
    datetime = models.DateField(auto_now_add=True)
    status = models.IntegerField(default=0, choices=[(0, 'Inactive'), (1, 'Active')])

    class Meta:
        db_table = "supplier_mstr"

