
from django.urls import path
from . import views

urlpatterns = [
    path('create_product', views.create_product, name='create_product'),
    path('<int:product_id>', views.detail , name = 'detail'),
    path('<int:product_id>/upvote' , views.upvote , name = 'upvote'),
]
