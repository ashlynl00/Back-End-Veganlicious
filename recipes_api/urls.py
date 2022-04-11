from django.urls import path
from . import views

urlpatterns = [
    path('api/recipes', views.RecipesList.as_view(), name='recipes_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/recipes/<int:pk>', views.RecipesDetail.as_view(), name='recipes_detail'), # api/contacts will be routed to the ContactDetail view for handling
]