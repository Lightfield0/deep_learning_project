from django.db import models

# Create your models here.
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    image_url = models.URLField()
    portfolio_url = models.URLField()

    def __str__(self):
        return self.name