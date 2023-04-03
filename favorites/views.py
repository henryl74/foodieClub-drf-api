from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from favorites.models import Favorite
from favorites.serializers import FavoriteSerializer

# Create your views here.


class FavoriteList(generics.ListCreateAPIView):
    """
    List all favorite instances and like a post if authenticated user
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()

    def perform_create(self, serializer):
        serializer.favorite(owner=self.request.user)


class FavoriteDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a favorite or delete it by id if you own it.
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()
