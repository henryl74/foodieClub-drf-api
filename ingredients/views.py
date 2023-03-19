from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Ingredients
from .serializers import IngredientsSerializer, IngredientsDetailSerializer

# Create your views here.


class IngredientsList(generics.ListCreateAPIView):
    """
    List ingredients of the recipes or create a recipe if logged in.
    """
    serializer_class = IngredientsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Ingredients.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class IngredientsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve ingredients recipe, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = IngredientsDetailSerializer
    queryset = Ingredients.objects.all()
