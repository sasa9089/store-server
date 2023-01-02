from django.urls import path

from products.views import products

app_name = 'products'
# index относится к главной странице продуктс
urlpatterns = [
    path('', products, name='index'),
]
