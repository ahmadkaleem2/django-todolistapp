from django.urls import path

from .views import add_todo, home_view,delete_todo
app_name = 'main'
urlpatterns = [
    path('',home_view),
    path('add_todo/',add_todo),
    path('delete_todo/<int:id>/',delete_todo),
]