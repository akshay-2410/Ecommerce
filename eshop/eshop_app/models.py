from django.db import models
from core.models import BaseModel


class Subcategories(BaseModel):
    name = models.CharField(max_length=255)
    image_subcatg = models.ImageField(null=True, upload_to='images/')


    def __str__(self):
        return self.name

class Categories(BaseModel):
    name = models.CharField(max_length=255)
    subcatg = models.ManyToManyField(Subcategories, blank=True)
    

    def __str__(self) -> str:
        return self.name

class Products(BaseModel):
    name = models.CharField(max_length=255)
    image_product = models.ImageField(null=True, upload_to='images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mrp = models.DecimalField(max_digits = 10, decimal_places = 2, null=True)
    subcategory = models.ManyToManyField(Subcategories, blank=True)
    category = models.ManyToManyField(Categories, blank=True)

    def __str__(self) -> str:
        return self.name