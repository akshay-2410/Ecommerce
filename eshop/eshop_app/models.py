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