from django.db import models

class MyPlants(models.Model):
    name = models.CharField(max_length=255, null=False)
    photo =  models.ImageField()
    last_watering_time = models.DateTimeField()
    place = models.ForeignKey('MyPlaces', on_delete=models.CASCADE)
    scientific_name = models.ForeignKey('Plants', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class MyPlaces(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name

class Plants(models.Model):
    name = models.CharField(max_length=255, null=False)
    water_every = models.TimeField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    sunlight = models.ForeignKey('Sunlight', on_delete=models.CASCADE)
    season = models.ForeignKey('Season', on_delete=models.CASCADE)
    soil = models.ForeignKey('Soil', on_delete=models.CASCADE)
    color = models.ForeignKey('Color', on_delete=models.CASCADE)  
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name

class Soil(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name

class Season(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name

class Sunlight(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name 

class Color(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name 