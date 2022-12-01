from django.db import models

class Stock_db(models.Model):
    ticker = models.CharField(max_length=10)

    def __str__(self):
        return self.ticker
