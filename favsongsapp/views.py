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
from django.http import HttpResponse

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

class OpinionListView(ListView):
    template_name = "opinionlist.html"
    model = Opinion
    context_object_name = "opinion_list"


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
    success_url = '/home'


class OpinionCreateView(CreateView):
    template_name = "opinioncreate.html"
    model = Opinion
    fields = ('__all__') 


class OpinionUpdateView(UpdateView):
    template_name = "opinionupdate.html"
    model = Opinion
    fields = ['song', 'opinion']


class OpinionDeleteView(DeleteView):
    template_name = "opiniondelete.html"
    model = Opinion
    success_url = '/home'


def fav_and_opinion_view(request):
   
    fav_list = Fav.objects.all()
    opinion_list = Opinion.objects.all()
    # print(fav_list)
    # print(opinion_list)
    context = {}
    context['favorite_list'] = fav_list
    context['opinion_list'] = opinion_list
    
    return render(request, 'rendering.html', context)
