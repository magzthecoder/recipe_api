from django.urls import path
from . import views

urlpatterns = [
    path('api/',views.get_recipes,name='get_recipes'),
    path('api/<int:id>/recipe',views.get_recipe,name='get_recipe'),
    path('api/<int:id>/recipe/update',views.update_recipe,name='update_recipe'),
    path('api/<int:id>/recipe/delete',views.delete_recipe,name='delete_recipe'),
    path('api/<int:id>/recipe/patch',views.patch_recipe,name='patch_recipe')
]