from django.db import models

class IPOCompany(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=50)
    issue_price = models.FloatField()
    lot_size = models.IntegerField()
    open_date = models.DateField()
    close_date = models.DateField()

    def __str__(self):
        return self.name
