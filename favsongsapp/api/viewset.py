from rest_framework import generics
from .serializers import FavSerializer, OpinionSerializer
from favsongsapp.models import Fav, Opinion
from .permissions import IsOwnerOrReadOnly


class FavListCreateAPIView(generics.ListCreateAPIView):
    queryset = Fav.objects.all()
    serializer_class = FavSerializer

class FavDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fav.objects.all()
    serializer_class = FavSerializer
    permission_classes = (IsOwnerOrReadOnly, )





class OpinionListCreatAPIView(generics.ListCreateAPIView):
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer 


class OpinionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer
    permission_classes = (IsOwnerOrReadOnly, )

