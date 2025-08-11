from django.shortcuts import render, redirect
from .models import Skills, Experience, Eduction, Testimonial, Project, Category
from math import ceil
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse

# Create your views here.


def home(request):
    skills = list(Skills.objects.all())
    experience = Experience.objects.all()
    education = Eduction.objects.all()
    testimonial = Testimonial.objects.all()
    category = Category.objects.all()
    project = Project.objects.all()
    half = ceil(len(skills) / 2)
    skills_left = skills[:half]
    skills_right = skills[half:]
    return render(
        request,
        "index.html",
        {
            "skills_left": skills_left,
            "skills_right": skills_right,
            "experiences": experience,
            "educations": education,
            "testimonials": testimonial,
            "categories": category,
            "projects": project,
        },
    )


from django.http import JsonResponse


def send_mail_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        message = f"From : {email}\n\nName : {name}\n\nMessage : {message}"

        if name and subject and message and email:
            try:
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [settings.EMAIL_HOST_USER],
                )
                return JsonResponse({"status": "success"})
            except Exception as e:
                return JsonResponse({"status": "error", "message": str(e)})
        else:
            return JsonResponse(
                {"status": "error", "message": "All fields are required"}
            )
