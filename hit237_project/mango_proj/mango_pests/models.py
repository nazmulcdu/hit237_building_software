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

class Farmer(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, default='')
    location = models.CharField(max_length=200)
    land_size = models.CharField(max_length=70, default='')

    def __str__(self):
        return f"{self.full_name} ({self.location})"

class PestReport(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='pest_reports', default=1)
    pest_name = models.CharField(max_length=100)
    date_of_observation = models.DateField(default=timezone.now)
    observation = models.TextField()
    severity_level = models.CharField(
        max_length=8,
        choices=[('Low','Low'), ('Medium','Medium'), ('High','High')],
        default='Low'
    )
    affected_stage = models.CharField(
        max_length=20,
        choices=[('Seedling','Seedling'), ('Vegetative','Vegetative'), ('Budding','Budding'),('Flowering','Flowering'), ('Fruiting','Fruiting'), ('Maturity','Maturity'), ('Harvest','Harvest')],default='Seedling')
    affected_farm_area = models.CharField(max_length=150, default='')
    symptoms = models.CharField(max_length=250, default='')
    image = models.ImageField(upload_to='pests/images/', blank=True, null=True)  # Make image optional
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pest_name} - {self.farmer} (Severity: {self.severity_level})"

class Treatment(models.Model):
    TREATMENT_TYPE_CHOICES = [
        ('Organic', 'Organic'),
        ('Chemical', 'Chemical'),
        ('Biological', 'Biological'),
        ('Mechanical', 'Mechanical'),
    ]

    APPLICATION_METHOD_CHOICES = [
        ('Spray', 'Spray'),
        ('Soil drench', 'Soil drench'),
        ('Injection', 'Injection'),
        ('Manual removal', 'Manual removal'),
    ]

    pest_report = models.ForeignKey(PestReport, on_delete=models.CASCADE, related_name='treatments', null=True, blank=True)
    treatment_type = models.CharField(max_length=50, choices=TREATMENT_TYPE_CHOICES, default='Organic')
    product_name = models.CharField(max_length=200)
    application_method = models.CharField(max_length=50, choices=APPLICATION_METHOD_CHOICES, default='Spray')
    application_date = models.DateField(default=timezone.now)
    is_organic = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product_name} for {self.pest_report.pest_name}"


