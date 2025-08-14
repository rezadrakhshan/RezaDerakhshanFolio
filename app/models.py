from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.postgres.fields import DateRangeField, ArrayField
import uuid

# Create your models here.


class Skills(models.Model):
    title = models.CharField(max_length=100)
    percentage = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )

    def __str__(self):
        return self.title


class Experience(models.Model):
    position = models.CharField(max_length=150)
    company = models.CharField(max_length=100)
    years = DateRangeField()
    tasks = ArrayField(models.TextField(), size=3)

    @property
    def years_display(self):
        start = self.years.lower.year
        end = "Present" if not self.years.upper else self.years.upper.year
        return f"{start} - {end}"

    def __str__(self):
        return self.company


class Eduction(models.Model):
    degree = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    years = DateRangeField()
    Institute = models.CharField(max_length=150)
    description = models.TextField()

    @property
    def years_display(self):
        start = self.years.lower.year
        end = "Present" if not self.years.upper else self.years.upper.year
        return f"{start} - {end}"

    def __str__(self):
        return self.degree


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    profile = models.ImageField(upload_to="media/testimonial/")
    comment = models.TextField()


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    client = models.CharField(max_length=100)
    date = models.DateField()
    url = models.URLField(null=True, blank=True)
    images_url = ArrayField(models.URLField(), size=5, blank=True, default=list)
    slug = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)

    def __str__(self):
        return self.title
