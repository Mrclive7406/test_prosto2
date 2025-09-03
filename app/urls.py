from django.urls import path
from . import views

urlpatterns = [
    path('export/player-levels/', views.export_player_level_data_csv,
         name='export_player_levels'),
]
