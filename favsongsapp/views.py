from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Fav, Opinion

# Create your views here.


class HomeFavView(TemplateView):
    template_name = "_base.html"


class AboutFavView(TemplateView):
    template_name = "about.html"


class FavListView(ListView):
    template_name = "favlist.html"
    model = Fav
    context_object_name = "fav_list"


class FavDetailView(DetailView):
    template_name = "favdetail.html"
    model = Fav


class OpinionDetailView(DetailView):
    template_name = "opiniondetail.html"
    model = Opinion


class FavCreateView(CreateView):
    template_name = "favcreate.html"
    model = Fav
    fields = ('__all__') 


class FavUpdateView(UpdateView):
    template_name = "favupdate.html"
    model = Fav
    fields = ['song_title', 'artist', 'album', 'year_of_release', 'rating']


class FavDeleteView(DeleteView):
    template_name = "favdelete.html"
    model = Fav
