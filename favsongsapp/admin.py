from django.contrib import admin
from .models import Fav, Opinion

# Register your models here.
@admin.register(Fav)
class FavAdmin(admin.ModelAdmin):
    list_display = ('song_title', 'artist', 'album', 'year_of_release', 'rating' , 'reviewer')
    list_filter = ('song_title', 'artist', 'album', 'year_of_release', 'rating' , 'reviewer')
    search_fields = ('song_title', 'artist', 'album', 'year_of_release', 'rating' , 'reviewer')

@admin.register(Opinion)
class OpinionAdmin(admin.ModelAdmin):
    list_display = ('song' , 'opinion' ,'reviewer')
    list_filter = ('song' , 'opinion' ,'reviewer')
    search_fields = ('song' , 'opinion' ,'reviewer')