from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=20)
    img_url = models.URLField(max_length=200) 
    
    
    def __str__(self):
        return self.name





class Car(models.Model):
    name = models.CharField(max_length=200,  default='Default Name')
    color = models.CharField(max_length=100)
    year = models.IntegerField()
    brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')
    model = models.CharField(max_length=100)
    img_url = models.URLField(max_length=200 , default='your_default_image_url')
    
    
