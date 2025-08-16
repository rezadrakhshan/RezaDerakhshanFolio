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
    path("experiences/", views.experience_page, name="experiences"),
    path("experiences/create/", views.experience_create_page, name="experience-create"),
    path("experiences/edit/<int:experience_id>/", views.experience_edit_page, name="experience-edit"),
    path("experiences/delete/<int:experience_id>/", views.experience_delete_page, name="experience-delete"),
    path("educations/", views.education_page, name="educations"),
    path("educations/create/", views.education_create_page, name="education-create"),
    path("educations/edit/<int:education_id>/", views.education_edit_page, name="education-edit"),
    path("educations/delete/<int:education_id>/", views.education_delete_page, name="education-delete"),
]
