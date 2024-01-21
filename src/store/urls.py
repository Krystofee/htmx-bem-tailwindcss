from django.urls import path
from . import views

urlpatterns = [
    path("authors", views.author_list_create_view, name="store-author-list-create"),
    path("authors/<int:id>/delete", views.author_delete_view, name="store-author-delete"),
]
