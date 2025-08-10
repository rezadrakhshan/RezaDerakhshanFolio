from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Skills(models.Model):
    title = models.CharField(max_length=100)
    percentage = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )

    def __str__(self):
        return self.title