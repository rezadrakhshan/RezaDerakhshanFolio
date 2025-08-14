from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("skills/", views.skill_page, name="skills"),
    path("skills/create/", views.skill_create_page, name="skill-create"),
    path("skills/edit/<int:skill_id>/", views.skill_edit_page, name="skill-edit"),
    path("skills/delete/<int:skill_id>/", views.skill_delete_page, name="skill-delete"),
]
