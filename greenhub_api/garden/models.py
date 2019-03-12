from django.db import models
from django.contrib.auth.models import User

class Plants(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    owner = models.ForeignKey('auth.User', related_name='plants', on_delete=models.CASCADE, blank=True, null=True)
    photo =  models.ImageField()
    last_watering_time = models.DateTimeField()
    place = models.ForeignKey('Places', on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name

class Places(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey('auth.User', related_name='places', on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.name

class Category(models.Model):
    SEASON_CHOICES = (
        ('SP', 'Spring',),
        ('SU', 'Summer',),
        ('A', 'autumn',),
        ('W', 'Winter',),
    )
    SUNLIGHT_CHOICES = (
        ('SL', 'Sunlight',),
        ('SH', 'Shadow',),
    )
    SOIL_CHOICES = (
        ('SA', 'sand',),
        ('SI', 'silt',),
        ('C', 'clay',),
    )

    name = models.CharField(max_length=255)
    owner = models.ForeignKey('auth.User', related_name='category', on_delete=models.CASCADE, blank=True, null=True)
    water_every = models.TimeField()
    sub_category = models.ForeignKey('SubCategory', on_delete=models.CASCADE,  blank=True, null=True)
    sunlight = models.CharField(max_length=2, choices=SUNLIGHT_CHOICES,)
    soil = models.CharField(max_length=2, choices=SOIL_CHOICES,)
    season = models.CharField(max_length=2, choices=SEASON_CHOICES,)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey('auth.User', related_name='subcategory', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

