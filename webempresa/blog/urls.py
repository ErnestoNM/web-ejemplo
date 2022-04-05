from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('category/<int:category_id>/', views.category, name='category')
]

"""
Se le pasa el int para convertir a entero lo que por defecto siempre
es una cadena.
"""

