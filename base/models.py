from decimal import Decimal
from django.db import models
from django.contrib import admin

class ConversionCategory(object):
    NONE = '1.0'
    MEGA = '1000000.0'
    KILO = '1000.0'
    MILLI = '0.001'
    MICRO = '0.000001'
    NANO = '0.000000001'
    PICO = '0.000000000001'

    CHOICES = (
        (NONE, "None"),
        (MEGA, "Mega"),
        (KILO, "Kilo"),
        (MILLI, "Milli"),
        (MICRO, "Micro"),
        (NANO, "Nano"),
        (PICO, "Pico")
    )

    CHOICES_SMALL = (
        (NONE, ""),
        (MEGA, "M"),
        (KILO, "k"),
        (MILLI, "m"),
        (MICRO, "&#181;"),
        (NANO, "n"),
        (PICO, "p")
    )

class ItemCategory(models.Model):

    name = models.CharField(max_length=200)

    suffix = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class Item(models.Model):

    name = models.CharField(max_length=100)
    
    category = models.ForeignKey(
        ItemCategory, related_name='+',
        null=True, blank=True)

    amperage = models.FloatField(
        null=True, blank=True)

    voltage = models.FloatField(
        null=True, blank=True)

    value_prefix = models.CharField(max_length=20,
        choices=ConversionCategory.CHOICES, 
        default=ConversionCategory.NONE,
        blank=True)

    value = models.FloatField(
        null=True, blank=True)

    value_conversion = models.FloatField(
        null=True, blank=True)

    item_number = models.CharField(
        max_length=100, null=True, blank=True)

    datasheet = models.CharField(
        max_length=200, null=True, blank=True)

    location = models.CharField(
        max_length=200, null=True, blank=True)

    notes = models.TextField(
        max_length=600, null=True, blank=True)

    quantity = models.IntegerField(null=True, blank=True)

    @property
    def category_full(self):
        if self.value_prefix:
            return dict(ConversionCategory.CHOICES)[self.value_prefix]
        else:
            return None

    def category_small(self):
        if self.value_prefix:
            return dict(ConversionCategory.CHOICES_SMALL)[self.value_prefix]
        else:
            return None


    def save(self, *args, **kwargs):
        # import ipdb; ipdb.set_trace()
        if self.value and self.value_prefix:
            self.value_conversion = float(self.value_prefix) * float(self.value)
        super(Item, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class ItemAdmin(admin.ModelAdmin):
    
    search_fields = ['name']

admin.site.register(ItemCategory)
admin.site.register(Item, ItemAdmin)