from django.db import models
from django.urls import reverse
from django.utils import timezone

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
    phone_number = models.CharField(max_length= 20, default='')
    location = models.CharField(max_length=200)
    land_size = models.CharField(max_length= 70, default='')
    pest_name = models.CharField(max_length=100)
    date_of_observation = models.DateField(default=timezone.now)
    observation = models.TextField()
    severity_level = models.CharField(max_length= 8, choices= [('Low','Low'), ('Medium','Medium'), ('High','High')], default='Low')
    affected_stage= models.CharField(choices=[('Seedling','Seedling'), ('Vegatative','Vegatative'), ('Budding','Budding'), ('Flowering','Flowering'), ('Fruiting','Fruiting'), ('Maturity','Maturity'), ('Harvest','Harvest')], default='Seedling')
    affected_farm_area= models.CharField(max_length=150, default='')
    symptoms= models.CharField(max_length=250, default='')
    image = models.ImageField(upload_to='pests/images/',blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.pest_name}"