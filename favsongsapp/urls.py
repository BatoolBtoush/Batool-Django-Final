from django.urls import path
from .views import (
    HomeFavView,
    AboutFavView,
    FavListView,
    FavDetailView,
    OpinionDetailView,
    FavCreateView,
    FavUpdateView,
    FavDeleteView,
)


urlpatterns = [
    path("fav-home", HomeFavView.as_view(), name="fav_home"),
    path("fav-about", AboutFavView.as_view(), name="fav_about"),
    path("fav-list", FavListView.as_view(), name="fav_list"),
    path("fav-detail/<int:pk>", FavDetailView.as_view(), name="fav_detail"),
    path("opinion-detail/<int:pk>", OpinionDetailView.as_view(), name="opinion_detail"),
    # path("fav-create/", FavCreateView.as_view(), name="fav_create"),
    # path("<int:pk>/fav-update/", FavUpdateView.as_view(), name="fav_update"),
    # path("<int:pk>/fav-delete/", FavDeleteView.as_view(), name="fav_delete"),
]
