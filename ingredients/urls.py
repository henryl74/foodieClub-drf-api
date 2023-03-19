from django.urls import path
from ingredients import views

urlpatterns = [
    path('ingredients/', views.IngredientsList.as_view()),
    path('ingredients/<int:pk>/', views.IngredientsDetail.as_view()),
]
