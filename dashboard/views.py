from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from app.models import *

# Create your views here.


@login_required(login_url="dashboard:login")
def index(request):
    return render(request, "admin/index.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("dashboard:index")
        else:
            messages.error(request, "invalid credentials")
            return redirect("dashboard:login")

    return render(request, "admin/login.html")


@login_required(login_url="dashboard:login")
def logout(request):
    auth.logout(request)
    return redirect("dashboard:login")


@login_required(login_url="dashboard:login")
def skill_page(request):
    skill = Skills.objects.all()
    return render(request, "admin/pages/skill.html", {"skills": skill})


@login_required(login_url="dashboard:login")
def skill_create_page(request):
    if request.method == "POST":
        title = request.POST.get("title")
        percentage = request.POST.get("percentage")
        if title and percentage:
            skill = Skills(title=title, percentage=percentage)
            skill.save()
            messages.success(request, "Skill created successfully")
            return redirect("dashboard:skills")
        else:
            messages.error(request, "All fields are required")
            return redirect("dashboard:skill-create")


@login_required(login_url="dashboard:login")
def skill_edit_page(request, skill_id):
    skill = Skills.objects.get(id=skill_id)
    if request.method == "POST":
        title = request.POST.get("title")
        percentage = request.POST.get("percentage")
        if title and percentage:
            skill.title = title
            skill.percentage = percentage
            skill.save()
            messages.success(request, "Skill updated successfully")
            return redirect("dashboard:skills")
        else:
            messages.error(request, "All fields are required")
            return redirect("dashboard:skills", skill_id=skill_id)


@login_required(login_url="dashboard:login")
def skill_delete_page(request, skill_id):
    skill = Skills.objects.get(id=skill_id)
    if request.method == "POST":
        skill.delete()
        messages.success(request, "Skill deleted successfully")
        return redirect("dashboard:skills")
