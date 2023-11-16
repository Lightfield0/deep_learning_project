from django.db import models
class YourModel(models.Model):
    # Diğer alanlar
    image = models.ImageField(upload_to='FusionFlowNet.jpg/')

# Create your models here.
