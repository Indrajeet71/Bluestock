from django.db import models

class IPOCompany(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=50, unique=True)
    issue_price = models.FloatField()
    price_band_min = models.FloatField(null=True, blank=True)
    price_band_max = models.FloatField(null=True, blank=True)
    lot_size = models.IntegerField()
    issue_size = models.CharField(max_length=50, null=True, blank=True)
    issue_type = models.CharField(max_length=50, null=True, blank=True)
    open_date = models.DateField()
    close_date = models.DateField()
    listing_date = models.DateField(null=True, blank=True)
    listing_price = models.FloatField(null=True, blank=True)
    market_price = models.FloatField(null=True, blank=True)
    rhp_pdf = models.FileField(upload_to='ipo_pdfs/', null=True, blank=True)
    drhp_pdf = models.FileField(upload_to='ipo_pdfs/', null=True, blank=True)

    @property
    def listing_gain(self):
        if self.listing_price and self.issue_price:
            return round(self.listing_price - self.issue_price, 2)
        return None

    @property
    def current_return(self):
        if self.market_price and self.issue_price:
            return round(((self.market_price - self.issue_price) / self.issue_price) * 100, 2)
        return None

    def save(self, *args, **kwargs):
        if self.close_date and self.open_date and self.close_date < self.open_date:
            raise ValueError("Close date cannot be before open date.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
