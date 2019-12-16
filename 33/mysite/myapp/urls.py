from django.urls import path

from myapp.views import main_page, number_id, create_product

urlpatterns = [
    path('', main_page),
    path('/<int:number>/',number_id),
    path('/<int:number>/<str:act>', create_product),
    # path('product/<int:number>/<slug:sl>', slug_name_product),



]