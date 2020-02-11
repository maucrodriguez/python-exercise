from seven import views
from django.urls import path

urlpatterns = [
  path('', views.seven_pairs, name='seven_pairs')
]