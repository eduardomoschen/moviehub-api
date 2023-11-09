from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie


class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        related_name='movies'
    )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'The rating must not be lower than 0 stars.'),
            MaxValueValidator(5, 'The rating must not be higher than 5 stars.')
        ]
    )
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.movie}'
