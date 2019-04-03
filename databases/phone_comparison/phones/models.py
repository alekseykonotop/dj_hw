from django.db import models


class Phone(models.Model):
    brand = models.TextField()
    model = models.TextField()
    cost = models.IntegerField()
    operating_system = models.TextField()
    cpu = models.TextField()  # Процессор
    display_size = models.FloatField()
    pixels_per_inch = models.IntegerField()
    duble_camera = models.BooleanField()
    number_of_SIM_cards = models.IntegerField()
    SIM_card_type = models.TextField()
    moisture_protection = models.BooleanField()


class IPhone(Phone):
    digital_zoom = models.BooleanField()


class Samsung(Phone):
    A_GPS_module = models.BooleanField()
    memory_card_support = models.TextField()
    max_size_memory_card = models.IntegerField()


class Xiaomi(Phone):
    graphic_accelerator = models.TextField()
