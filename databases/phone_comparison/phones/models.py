from django.db import models


class Phone(models.Model):
    """Model representing an phone."""

    brand = models.TextField()
    model = models.TextField()
    memory = models.IntegerField()
    cost = models.IntegerField()
    operating_system = models.TextField()
    cpu = models.TextField()
    display_size = models.FloatField()
    pixels_per_inch = models.IntegerField()
    duble_camera = models.BooleanField()
    number_of_SIM_cards = models.IntegerField()
    SIM_card_type = models.TextField()
    moisture_protection = models.BooleanField()

    class Meta:
        ordering = ['brand', 'model', 'memory']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.brand} {self.model} {self.memory} Gb'


class IPhone(Phone):
    digital_zoom = models.BooleanField()


class Samsung(Phone):
    A_GPS_module = models.BooleanField()
    memory_card_support = models.TextField()
    max_size_memory_card = models.IntegerField()


class Xiaomi(Phone):
    graphic_accelerator = models.TextField()
