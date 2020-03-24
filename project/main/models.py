from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

# Create your models here.
def max_year():
    year = datetime.date.today().year
    return year

class MovieEntry(models.Model):
    app_label = 'main'
    min_year = 1900
    movie_title = models.CharField(max_length = 100)
    dvd_name = models.CharField(max_length = 100, blank = True)
    form_field = models.CharField(max_length = 100, blank = True)
    genre = models.CharField(max_length = 100, blank = True)
    year = models.IntegerField(blank = True, default = min_year, validators = [MinValueValidator(min_year), MaxValueValidator(max_year())])
    alt_title_1 = models.CharField(max_length = 100, blank = True)
    alt_title_2 = models.CharField(max_length = 100, blank = True)
    count  = models.CharField(max_length = 100, blank = True)
    director = models.CharField(max_length = 100, blank = True)
    language = models.CharField(max_length = 100, blank = True)
    date_watched = models.DateField(auto_now=False, auto_now_add=False)
    spec = models.CharField(max_length = 100, blank = True)

    def __str__(self):
        return f"{self.movie_title} {self.year}"