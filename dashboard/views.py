from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from app.models import *
import boto3
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import uuid

# Create your views here.


def get_s3_client():
    return boto3.client(
        "s3",
        endpoint_url=settings.AWS_S3_ENDPOINT_URL,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )


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


@login_required(login_url="dashboard:login")
def experience_page(request):
    experiences = Experience.objects.all()
    return render(request, "admin/pages/experience.html", {"experiences": experiences})


@login_required(login_url="dashboard:login")
def experience_create_page(request):
    if request.method == "POST":
        position = request.POST.get("position")
        company = request.POST.get("company")
        years = request.POST.get("years")
        tasks = request.POST.get("tasks")

        years_format = years.split("-")
        years = [f"{y.strip()}-01-01" for y in years_format]
        if len(years) != 2:
            messages.info(request, "Years must be in the format YYYY - YYYY")
            return redirect("dashboard:experiences")
        tasks = tasks.split(",") if tasks else []
        if position and company and years and tasks:
            experience = Experience(
                position=position, company=company, years=years, tasks=tasks
            )
            experience.save()
            messages.success(request, "Experience created successfully")
            return redirect("dashboard:experiences")

    return redirect("dashboard:experiences")


@login_required(login_url="dashboard:login")
def experience_edit_page(request, experience_id):
    experience = Experience.objects.get(id=experience_id)
    if request.method == "POST":
        position = request.POST.get("position")
        company = request.POST.get("company")
        years = request.POST.get("years")
        tasks = request.POST.get("tasks")
        years_format = years.split("-")
        years = [f"{y.strip()}-01-01" for y in years_format]
        if len(years) != 2:
            messages.info(request, "Years must be in the format YYYY - YYYY")
            return redirect("dashboard:experiences")
        tasks = tasks.split(",") if tasks else []
        if position and company and years and tasks:
            experience.position = position
            experience.company = company
            experience.years = years
            experience.tasks = tasks
            experience.save()
            messages.success(request, "Experience updated successfully")
            return redirect("dashboard:experiences")


@login_required(login_url="dashboard:login")
def experience_delete_page(request, experience_id):
    experience = Experience.objects.get(id=experience_id)
    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience deleted successfully")
        return redirect("dashboard:experiences")


@login_required(login_url="dashboard:login")
def education_page(request):
    educations = Eduction.objects.all()
    return render(request, "admin/pages/education.html", {"educations": educations})


@login_required(login_url="dashboard:login")
def education_create_page(request):
    if request.method == "POST":
        degree = request.POST.get("degree")
        field = request.POST.get("field")
        institution = request.POST.get("Institute")
        years = request.POST.get("years")
        description = request.POST.get("description")

        years_format = years.split("-")
        years = [f"{y.strip()}-01-01" for y in years_format]
        if len(years) != 2:
            messages.info(request, "Years must be in the format YYYY - YYYY")
            return redirect("dashboard:educations")
        if degree and field and institution and years and description:
            education = Eduction(
                degree=degree,
                field=field,
                Institute=institution,
                years=years,
                description=description,
            )
            education.save()
            messages.success(request, "Education created successfully")
            return redirect("dashboard:educations")


@login_required(login_url="dashboard:login")
def education_edit_page(request, education_id):
    education = Eduction.objects.get(id=education_id)
    if request.method == "POST":
        degree = request.POST.get("degree")
        field = request.POST.get("field")
        institution = request.POST.get("Institute")
        years = request.POST.get("years")
        description = request.POST.get("description")
        years_format = years.split("-")
        years = [f"{y.strip()}-01-01" for y in years_format]
        if len(years) != 2:
            messages.info(request, "Years must be in the format YYYY - YYYY")
            return redirect("dashboard:educations")
        if degree and field and institution and years and description:
            education.degree = degree
            education.field = field
            education.Institute = institution
            education.years = years
            education.description = description
            education.save()
            messages.success(request, "Education updated successfully")
            return redirect("dashboard:educations")


@login_required(login_url="dashboard:login")
def education_delete_page(request, education_id):
    education = Eduction.objects.get(id=education_id)
    if request.method == "POST":
        education.delete()
        messages.success(request, "Education deleted successfully")
        return redirect("dashboard:educations")


@login_required(login_url="dashboard:login")
def category_page(request):
    categories = Category.objects.all()
    return render(request, "admin/pages/category.html", {"categories": categories})


@login_required(login_url="dashboard:login")
def category_create_page(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            category = Category(title=title)
            category.save()
            messages.success(request, "Category created successfully")
            return redirect("dashboard:categories")
        else:
            messages.error(request, "Title is required")
            return redirect("dashboard:category-create")


@login_required(login_url="dashboard:login")
def category_edit_page(request, category_id):
    category = Category.objects.get(slug=category_id)
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            category.title = title
            category.save()
            messages.success(request, "Category updated successfully")
            return redirect("dashboard:categories")


@login_required(login_url="dashboard:login")
def category_delete_page(request, category_id):
    category = Category.objects.get(slug=category_id)
    if request.method == "POST":
        category.delete()
        messages.success(request, "Category deleted successfully")
        return redirect("dashboard:categories")


@login_required(login_url="dashboard:login")
def testimonial_page(request):
    testimonials = Testimonial.objects.all()
    return render(
        request, "admin/pages/testimonial.html", {"testimonials": testimonials}
    )


@csrf_exempt
@login_required(login_url="dashboard:login")
def testimonial_create_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        position = request.POST.get("position")
        profile_image = request.FILES.get("profile")
        comment = request.POST.get("comment")

        if name and position and profile_image and comment:
            try:
                s3_client = get_s3_client()
                file_name = f"testimonials/{uuid.uuid4()}_{profile_image.name}"

                s3_client.upload_fileobj(
                    profile_image, settings.AWS_STORAGE_BUCKET_NAME, file_name
                )

                file_url = f"https://storage.c2.liara.space/{settings.AWS_STORAGE_BUCKET_NAME}/{file_name}"

                testimonial = Testimonial(
                    name=name, position=position, profile=file_url, comment=comment
                )
                testimonial.save()
                messages.success(request, "Testimonial created successfully")
                return redirect("dashboard:testimonials")

            except Exception as e:
                return JsonResponse({"error": str(e)}, status=500)


@login_required(login_url="dashboard:login")
def testimonial_edit_page(request, testimonial_id):
    testimonial = Testimonial.objects.get(id=testimonial_id)
    if request.method == "POST":
        name = request.POST.get("name")
        position = request.POST.get("position")
        profile_image = request.FILES.get("profile")
        comment = request.POST.get("comment")

        if name and position and comment:
            try:
                if profile_image:
                    s3_client = get_s3_client()
                    file_url = testimonial.profile
                    bucket_prefix = f"https://storage.c2.liara.space/{settings.AWS_STORAGE_BUCKET_NAME}/"

                    file_key = file_url.replace(bucket_prefix, "")

                    s3_client.delete_object(
                        Bucket=settings.AWS_STORAGE_BUCKET_NAME,
                        Key=file_key
                    )


                    file_name = f"testimonials/{uuid.uuid4()}_{profile_image.name}"

                    s3_client.upload_fileobj(
                        profile_image, settings.AWS_STORAGE_BUCKET_NAME, file_name
                    )

                    file_url = f"https://storage.c2.liara.space/{settings.AWS_STORAGE_BUCKET_NAME}/{file_name}"
                    testimonial.profile = file_url

                testimonial.name = name
                testimonial.position = position
                testimonial.comment = comment
                testimonial.save()
                messages.success(request, "Testimonial updated successfully")
                return redirect("dashboard:testimonials")

            except Exception as e:
                return JsonResponse({"error": str(e)}, status=500)

@login_required(login_url="dashboard:login")
def testimonial_delete_page(request, testimonial_id):
    testimonial = Testimonial.objects.get(id=testimonial_id)
    if request.method == "POST":
        try:
            s3_client = get_s3_client()
            file_url = testimonial.profile
            bucket_prefix = f"https://storage.c2.liara.space/{settings.AWS_STORAGE_BUCKET_NAME}/"

            file_key = file_url.replace(bucket_prefix, "")

            s3_client.delete_object(
                Bucket=settings.AWS_STORAGE_BUCKET_NAME,
                Key=file_key
            )

            testimonial.delete()
            messages.success(request, "Testimonial deleted successfully")
            return redirect("dashboard:testimonials")

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)