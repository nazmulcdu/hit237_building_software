from django.db import models
from django.urls import reverse

class Pest(models.Model):
    name = models.CharField(max_length=200)
    scientific_name = models.CharField(max_length=200)
    short_desc = models.TextField()
    full_desc = models.TextField()
    image = models.ImageField(upload_to='pests/images/')
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('pest_detail', args=[str(self.id)])

class Symptom(models.Model):
    pest = models.ForeignKey(Pest, on_delete=models.CASCADE, related_name='symptoms')
    description = models.TextField()
    affected_part = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.pest.name} - {self.affected_part}"

class Treatment(models.Model):
    pest = models.ForeignKey(Pest, on_delete=models.CASCADE, related_name='treatments')
    name = models.CharField(max_length=200)
    description = models.TextField()
    is_organic = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.pest.name} - {self.name}"

class PestReport(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    location = models.CharField(max_length=200)
    pest_name = models.CharField(max_length=100)
    observation = models.TextField()
    image = models.ImageField(upload_to='pests/images/',blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.pest_name}"