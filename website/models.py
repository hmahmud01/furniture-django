from django.db import models


class AreaName(models.Model):
    EAST = 'EAST'
    WEST = 'WEST'
    NORTH = 'NORTH'
    SOUTH = 'SOUTH'
    CENTRAL = 'CENTRAL'

    AREA_CHOICES = [
        (EAST, 'East'),
        (WEST, 'West'),
        (NORTH, 'North'),
        (SOUTH, 'South'),
        (CENTRAL, 'Central'),
    ]

    area = models.CharField(max_length=50, choices=AREA_CHOICES, default=EAST)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.area

class ShopName(models.Model):
    area = models.ForeignKey(AreaName, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    addr = models.CharField(max_length=250, null=True, blank=True)
    hours = models.FloatField(null = True, blank=True)
    email = models.CharField(max_length=150, null=True, blank=True)
    delivary = models.CharField(max_length=350, null=True, blank=True)
    service = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name
    
class ContactPerson(models.Model):
    shop = models.ForeignKey(ShopName, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name

class Furniture(models.Model):
    shop = models.ForeignKey(ShopName ,on_delete=models.CASCADE)
    title = models.CharField(max_length=150, null=True, blank=True)
    subtitle = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField('furniture_image', upload_to='furnitures', blank=True, null=True)
    status = models.BooleanField(null=True, blank=True, default=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)
    reference = models.CharField(max_length=150, null=True, blank=True)
    offer = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.title
    

class Order(models.Model):
    email = models.CharField(max_length=150, null=True, blank=True)
    msg = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class OrderedFurniture(models.Model):
    furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)