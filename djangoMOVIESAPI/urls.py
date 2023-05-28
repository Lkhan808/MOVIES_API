from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from djangoMOVIESAPI import settings
from movies.views import movie_list_create_api_view, movie_api_view, directors_list_create_view, \
    directors_api_put_view, genre_list_create_view, genre_api_put_view

from drf_spectacular.views import SpectacularRedocView, SpectacularSwaggerView, SpectacularAPIView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/movies/', movie_list_create_api_view),
    path('api/movies/<int:id>/', movie_api_view),
    path('api/directors/', directors_list_create_view),
    path('api/directors/<int:id>/', directors_api_put_view),
    path('api/genres/', genre_list_create_view),
    path('api/genres/<int:id>/', genre_api_put_view),
    path('doc/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger_ui'),
    path('api/schema/redoc', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('schema/', SpectacularAPIView.as_view(), name='schema')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)