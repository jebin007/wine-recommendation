from django.db import models

import numpy as np
# Create your models here.

class Wine(models.Model):
    name = models.CharField(max_length=200)

    def average_rating(self):
        all_ratings = list(x.rating for x in self.review_set.all())
        # all_ratings is equivalent to map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)

    def __str__(self):
        return self.name


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date_published')
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)