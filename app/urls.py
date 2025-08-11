from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path("", views.home, name="home"),
    path("send-mail", views.send_mail_page, name="send-mail"),
    path("project/<slug>", views.project_detail, name="project-detail"),
]
