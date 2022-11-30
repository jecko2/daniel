from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.landing_home_view, name="home_view"),
    path("posts/<int:year>/<int:month>/<int:day>/<str:slug>/", views.post_detail_view, name="post_detail"),
    path("posts/<str:tag>/", views.post_list_per_tag_view, name="post_list_per_tag"),
]
