from django.urls import path

from users.views import login, registration
app_name = 'users'
# index относится к главной странице продуктс
urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),

]
