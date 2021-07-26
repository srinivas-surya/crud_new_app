
from django.urls import path

from . import views

urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('profile_create/', views.profile_create, name='profile_create'),
    path('profile_data/', views.profile_data, name='profile_data'),
    path('profile_update/<int:pk>', views.profile_update, name='profile_update'),
    path('profile_delete/<int:pk>', views.profile_delete, name='profile_delete')
]