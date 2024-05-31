from django.db import models


class SearchRequest(models.Model):
    DS_CHOICES = (
        ('wikir', 'wikir'),
        ('antique', 'antique'),
    )

    dataset = models.CharField(max_length=10, choices=DS_CHOICES, default='wiki')
    search_field = models.CharField(max_length=256)
