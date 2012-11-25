import random
from base.models import Item, ConversionCategory, ItemCategory

    # name = models.CharField(max_length=100, null=True, blank=True)
    
    # category = models.ForeignKey(
    #     ItemCategory, related_name='+')

    # amperage = models.DecimalField(
    #     decimal_places=2, max_digits=10, null=True, blank=True)

    # voltage = models.DecimalField(
    #     decimal_places=2, max_digits=10, null=True, blank=True)

    # value_prefix = models.CharField(max_length=20,
    #     choices=ConversionCategory.CHOICES, 
    #     default=ConversionCategory.NONE)

    # value = models.DecimalField(
    #     decimal_places=15, max_digits=20, null=True, blank=True)

    # value_conversion = models.DecimalField(
    #     decimal_places=15, max_digits=20, null=True, blank=True)

    # item_number = models.CharField(
    #     max_length=100, null=True, blank=True)

    # datasheet = models.CharField(
    #     max_length=200, null=True, blank=True)

    # location = models.CharField(
    #     max_length=200, null=True, blank=True)

    # quantity = models.IntegerField(null=True, blank=True)

def run():

    Item.objects.all().delete()
    
    for i in range(100):

        Item.objects.create(**{
            "name": "Test Item %s" % i,
            "category": ItemCategory.objects.all()[0],
            "amperage": random.uniform(1.0, 1000.0),
            "voltage": random.uniform(1.0, 1000.0),
            "value_prefix": random.choice([x for x,y in ConversionCategory.CHOICES]),
            "value": random.uniform(1.0, 1000.0),
            "item_number": "ABCDEF%s" % i,
            "datasheet": "http://www.datasheet.com/%s/" % i,
            "location": "Somewhere",
            "quantity": random.randint(1,1000)
        })