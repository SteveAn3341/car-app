from django.urls import path
from . import views


urlpatterns = [
    path('', views.init, name = 'index'),
    path('brands/<int:id>/',views.details, name = 'brand_id'),
    path('model/<int:id>/',views.models, name = 'car_models'),
    path('individual/<int:id>/',views.individual, name = 'individual'),
    path('add_brand/', views.add_brand, name='add_brand'),
    path('update_brand/<int:id>/', views.update_brand, name='update_brand'),
    path('delete_brand/<int:id>/', views.delete_brand, name='delete_brand'),
     path('add_car_model/', views.add_car_model, name='add_car_model'),
    path('delete_car_model/<int:id>/', views.delete_car_model, name='delete_car_model'),
    path('add_car_details/', views.add_car_details, name = 'details')

    
    
]   
