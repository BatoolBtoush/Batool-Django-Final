from rest_framework import generics
from .serializers import FavSerializer, OpinionSerializer
from favsongsapp.models import Fav, Opinion


class FavListAPIView(generics.ListAPIView):
    queryset = Fav.objects.all()
    serializer_class = FavSerializer


class FavCreateAPIView(generics.ListCreateAPIView):
    queryset = Fav.objects.all()
    serializer_class = FavSerializer


class FavDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fav.objects.all()
    serializer_class = FavSerializer


class OpinionListAPIView(generics.ListAPIView):
    queryset = Opinion.objects.all()
    serializer_class = FavSerializer

class OpinionCreatAPIView(generics.ListCreateAPIView):
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer


class OpinionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer

