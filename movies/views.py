from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

from movies.models import Movies, Director, Genre
from movies.serializers import *


@api_view(["GET", "POST"])
def movie_list_create_api_view(request):
    if request.method == "GET":
        movies = Movies.objects.all()
        data = MovieSerializer(movies, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        data = request.data
        movie = Movies.objects.create(
            title=data.get('title'),
            description=data.get('description'),
            director_id=data.get('director_id'),
            rate=data.get('rate')
        )
        movie.genre.set(data.get('genre'))
        return Response(data=MovieSerializer(movie, many=False).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_api_view(request, **kwargs):
    movie = Movies.objects.get(id=kwargs['id'])
    if request.method == 'GET':
        data = MovieRetrieveSerializer(movie, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        data = request.data
        movie.director_id = data.get('director_id')
        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.genre.set(data.get('genres'))
        movie.rate = data.get('rate')
        movie.save()
        return Response(data=MovieRetrieveSerializer(movie, many=False).data, status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        data = request.data
        movie.id = data.get('id', None)
        movie.delete()
        return Response({'message': f'Movie {movie.title} is deleted'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def directors_list_create_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        data = DirectorSerializer(directors, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        data = request.data
        director = Director.objects.create(
            name=data.get('name')
        )
        return Response(data=DirectorRetrieveSerializer(director, many=False).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def directors_api_put_view(request, **kwargs):
    director = Director.objects.get(id=kwargs['id'])
    if request.method == 'GET':
        data = DirectorRetrieveSerializer(director, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        data = request.data
        director.name = data.get('name')
        director.save()
        return Response(data=DirectorRetrieveSerializer(director, many=False).data, status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        data = request.data
        director.id = data.get('id', None)
        director.delete()
        return Response({'message': f'Director {director.name} is deleted'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def genre_list_create_view(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        data = GenreSerializer(genres, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        data = request.data
        genre = Genre.objects.create(
            name=data.get('name'),
        )
        return Response(data=GenreSerializer(genre, many=False).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def genre_api_put_view(request, **kwargs):
    genre = Genre.objects.get(id=kwargs['id'])
    if request.method == 'GET':
        data = GenreSerializer(genre, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        data = request.data
        genre.name = data.get('name')
        genre.save()
        return Response(data=GenreSerializer(genre, many=False).data, status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        data = request.data
        genre.id = data.get('id', None)
        genre.delete()
        return Response({'message': f'Genre {genre.name} is deleted'}, status=status.HTTP_204_NO_CONTENT)


class MovieDirectorAPIView(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        director = self.kwargs.get('director_name')
        queryset = Movies.objects.filter(director=director)
        return queryset


@api_view()
def movie_genre_api_view(request, genre):
    movies = Movies.objects.filter(genre=genre)
    data = MovieSerializer(movies, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)
