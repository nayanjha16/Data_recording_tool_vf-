from django.urls import path
from . import views


urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('upload_audio', views.upload_audio, name="upload_audio"),
    path('thankyou', views.thankyou, name="thankyou")
]
