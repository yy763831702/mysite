from django.urls import path
from . import views

app_name = 'forums'
urlpatterns = [
    path('', views.index, name = 'index'),



    path("<single_slug>/<str:slug>/", views.list, name = 'list'),
    path("<single_slug>/<str:slug>/<int:forum_id>/", views.detail, name = 'detail'),
    path("<single_slug>/", views.single_slug, name="single_slug"),
]
