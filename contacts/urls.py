from . import views
from django.urls import path


app_name="contact"
urlpatterns = [
    path("subscribe/", views.subscribe, name="subscribe")
]
