from django.urls import path
from . import views



urlpatterns = [
    path('' , views.category , name="Categories"),
    path('<int:id>' , views.getCategoryById , name="Get Category by ID"),
    path('<slug:slug>' , views.getCategoryBySlug , name="Get Category by Slug"),
]
