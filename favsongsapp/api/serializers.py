from rest_framework import serializers
from favsongsapp.models import Fav, Opinion


class FavSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fav
        fields = '__all__'


class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinion
        fields = '__all__'


