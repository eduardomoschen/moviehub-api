from django.urls import path
from movies import views

urlpatterns = [
    path(
        'movies/',
        views.MovieCreateListView.as_view(),
        name='movie-create-view'
    ),

    path(
        'movies/<int:pk>/',
        views.MovieRetrieveUpdateDestroyView.as_view(),
        name='movie-detail-view'
    ),
]
