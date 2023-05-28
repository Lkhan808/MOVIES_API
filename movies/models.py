from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self): return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self): return self.name


class Movies(models.Model):
    director = models.ForeignKey(Director, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name='director_movies')
    genre = models.ManyToManyField(Genre, blank=True)
    preview = models.ImageField(upload_to='previews', blank=True)
    title = models.CharField(max_length=256)
    description = models.TextField()
    rate = models.FloatField(default=0)

    def __str__(self): return self.title

    @property
    def filtered_reviews(self):
        return self.reviews.all()

    @property
    def director_name(self):
        return self.director.name if self.director else 'None'


STAR_CHOISES = (
    (1, '* '),
    (2, 2 * '* '),
    (3, 3 * '* '),
    (4, 4 * '* '),
    (5, 5 * '* '),
)


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(default=5, choices=STAR_CHOISES)

    def __str__(self): return self.text

