from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:doc_id>/edit", views.doc_edit, name="doc_edit"),
    path("<int:doc_id>/view", views.doc_view, name="doc_view"),
]