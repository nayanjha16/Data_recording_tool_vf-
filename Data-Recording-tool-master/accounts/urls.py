from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('user_id_map/', views.print_user_id_map, name="user_id_map")
]
