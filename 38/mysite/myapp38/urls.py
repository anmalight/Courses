from django.urls import path
from django.views.generic.base import TemplateView

from .views import first_page, second_page, third_page, fourth_page, animal_list, animal_id, animal_new

urlpatterns = [
    path('', first_page),
    path('new/', second_page),
    path('final/', third_page),
    path('verynew/', fourth_page),
    path('animal/<int:animal_id>/', animal_id, name='animal_id'),
    path('animal/', animal_list, name='animal_list'),
    path('add-animal-form/', animal_new, name='animal_new'),







]