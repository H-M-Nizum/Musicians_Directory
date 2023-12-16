from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_album_view.as_view(), name='add_album'),
    path('edit/<int:id>', views.edit_album_view.as_view(), name='edit_album'),
    path('delete/<int:id>', views.delete_album, name='delete_album'),
]