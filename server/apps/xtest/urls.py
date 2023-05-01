from django.urls import path
from . import views

urlpatterns = [
    path("form/", views.getForm),
    path("post_form", views.postForm),
]