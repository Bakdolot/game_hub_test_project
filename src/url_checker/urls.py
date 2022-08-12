from django.urls import path

from . import views

app_name = 'url_checker'

urlpatterns = [
    path("links/", views.link_list, name="links"),
    path("link/<int:link_id>", views.check_link, name="check_link"),
]
