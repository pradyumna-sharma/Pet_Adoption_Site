from django.urls import path
from . import views

app_name = 'pets'

urlpatterns = [
    path('', views.pet_list, name='pet_list'),
    path('pets/<int:pet_id>/', views.pet_detail, name='pet_detail'),
    path('pets/<int:pet_id>/adopt/', views.adoption_form, name='adoption_form'),
    path('pets/<int:pet_id>/submit-adoption/', views.adopt_pet, name='adopt_pet'),
]
