from django.db import models

class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name="Имя")
    order_phone = models.CharField(max_length=200, verbose_name="Номер")
    order_email - models.CharField(max_length=50, verbose_name="Email")