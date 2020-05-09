from django.urls import path
from . import views

app_name = 'forums'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:forum_id>/', views.detail, name = 'detail'),
    path('<int:forum_id>/results', views.results, name = 'results'),
    path("<single_slug>", views.single_slug, name="single_slug"),

]
