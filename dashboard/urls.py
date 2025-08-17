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
    path("categories/", views.category_page, name="categories"),
    path("categories/create/", views.category_create_page, name="category-create"),
    path("categories/edit/<str:category_id>/", views.category_edit_page, name="category-edit"),
    path("categories/delete/<str:category_id>/", views.category_delete_page, name="category-delete"),
    path("testimonials/", views.testimonial_page, name="testimonials"),
    path("testimonials/create/", views.testimonial_create_page, name="testimonial-create"),
    path("testimonials/edit/<int:testimonial_id>/", views.testimonial_edit_page, name="testimonial-edit"),
    path("testimonials/delete/<int:testimonial_id>/", views.testimonial_delete_page, name="testimonial-delete"),
]
