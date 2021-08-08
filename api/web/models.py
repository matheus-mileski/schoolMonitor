from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True

class Bme280(BaseModel):
    temperature = models.DecimalField(
        blank=False,
        decimal_places=2,
        max_digits=5,
    )

    umidity = models.DecimalField(
        blank=False,
        decimal_places=2,
        max_digits=6,
    )

    pressure = models.DecimalField(
        blank=False,
        decimal_places=2,
        max_digits=6,
    )

class Ccs811(BaseModel):
    co2 = models.IntegerField(
        blank=False,
        max_digits=5,
    )

    tvoc = models.IntegerField(
        blank=False,
        max_digits=5,
    )
