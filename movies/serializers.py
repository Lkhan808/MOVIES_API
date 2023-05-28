from rest_framework import serializers

from movies.models import Movies, Director, Genre, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text stars'.split()


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(many=False)
    genre = GenreSerializer(many=True)
    filtered_reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movies
        fields = ('id', 'title', 'preview', 'director_name', 'director', 'genre', 'filtered_reviews')


class MovieRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class DirectorRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    director_id = serializers.IntegerField()
    director = serializers.CharField(required=False)
    rate = serializers.FloatField()
    genre = serializers.ListField()