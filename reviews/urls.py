from django.urls import path
from reviews import views

urlpatterns = [
    path(
        'reviews/',
        views.ReviewCreateListView.as_view(),
        name='review-create-view'
    ),

    path(
        'reviews/<int:pk>/',
        views.ReviewRetrieveUpdateDestroyView.as_view(),
        name='review-detail-view'
    ),
]
