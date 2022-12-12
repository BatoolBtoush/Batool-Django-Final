from django.urls import path

from .views import (
    HomeFavView,
    AboutFavView,
    FavListView,
    FavDetailView,
    OpinionListView,
    OpinionDetailView,
    FavCreateView,
    FavUpdateView,
    FavDeleteView,
    OpinionCreateView,
    OpinionUpdateView,
    OpinionDeleteView,
    fav_and_opinion_view
)

from favsongsapp.api.viewset import FavListAPIView, OpinionListAPIView, FavDetailAPIView, OpinionDetailAPIView


urlpatterns = [
    path("fav-home", HomeFavView.as_view(), name="fav_home"),
    path("fav-about", AboutFavView.as_view(), name="fav_about"),
    path("fav-list", FavListView.as_view(), name="fav_list"),
    path("fav-detail/<int:pk>", FavDetailView.as_view(), name="fav_detail"),
    path("opinion-list", OpinionListView.as_view(), name="opinion_list"),
    path("opinion-detail/<int:pk>", OpinionDetailView.as_view(), name="opinion_detail"),
    path("fav-create/", FavCreateView.as_view(), name="fav_create"),
    path("fav-update/<int:pk>", FavUpdateView.as_view(), name="fav_update"),
    path("fav-delete/<int:pk>", FavDeleteView.as_view(), name="fav_delete"),
    path("opinion-create/", OpinionCreateView.as_view(), name="opinion_create"),
    path("opinion-update/<int:pk>", OpinionUpdateView.as_view(), name="opinion_update"),
    path("opinion-delete/<int:pk>", OpinionDeleteView.as_view(), name="opinion_delete"),
    path('fav-and-opinion', fav_and_opinion_view, name='fav_and_opinion'),
    path('api/fav-list',FavListAPIView.as_view(), name='api_fav_list'),
    path('api/opinion-list',OpinionListAPIView.as_view(), name='api_opinion_list'),
    path('api/fav-detail/<int:pk>',FavDetailAPIView.as_view(), name='api_fav_detail'),
    path('api/opinion-detail/<int:pk>',OpinionDetailAPIView.as_view(), name='api_opinion_detail'),
    



]
