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


class Temperature(BaseModel):
    value = models.DecimalField(
        blank=False,
        decimal_places=2,
        max_digits=5,
    )

    topic = models.TextField(
        blank=False,
    )


class Humidity(BaseModel):
    value = models.DecimalField(
        blank=False,
        decimal_places=2,
        max_digits=6,
    )

    topic = models.TextField(
        blank=False,
    )


class Pressure(BaseModel):
    value = models.DecimalField(
        blank=False,
        decimal_places=2,
        max_digits=6,
    )

    topic = models.TextField(
        blank=False,
    )


class Co2(BaseModel):
    value = models.IntegerField(
        blank=False,
    )

    topic = models.TextField(
        blank=False,
    )


class Tvoc(BaseModel):
    value = models.IntegerField(
        blank=False,
    )

    topic = models.TextField(
        blank=False,
    )
