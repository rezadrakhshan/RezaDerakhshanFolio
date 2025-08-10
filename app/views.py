from django.shortcuts import render
from .models import Skills, Experience
from math import ceil

# Create your views here.


def home(request):
    skills = list(Skills.objects.all())
    experience = Experience.objects.all()
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
        },
    )
