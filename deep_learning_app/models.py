from django.db import models

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField()
    # photo = models.ImageField(upload_to='deep_learning_app/static/team_photos/', default='deep_learning_app/static/default-user.png')
    photo = models.ImageField(upload_to='team_photos/', default='default-user.png')
    portfolio_url = models.URLField(blank=True)

    def __str__(self):
        return self.name
