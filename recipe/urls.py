from django.urls import path
from . import views

urlpatterns = [
    path('api/',views.get_recipes,name='get_recipes'),
    path('api/<int:id>/recipe',views.get_recipe,name='get_recipe')
]