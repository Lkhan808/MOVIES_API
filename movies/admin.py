from django.contrib import admin

from movies.models import Movies, Director, Genre, Review

admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Movies)
admin.site.register(Review)