from django.contrib.auth.models import User
from django.db import connection
from django.shortcuts import render, redirect
from django.utils import timezone

from app.models import Climber, Expedition, ClimberExpedition


def index(request):
    name = request.GET.get("name", "")
    climbers = Climber.objects.filter(name__icontains=name).filter(status=1)
    draft_expedition = get_draft_expedition()

    context = {
        "name": name,
        "climbers": climbers
    }

    if draft_expedition:
        context["climbers_count"] = len(draft_expedition.get_climbers())
        context["draft_expedition"] = draft_expedition

    return render(request, "home_page.html", context)


def add_climber_to_draft_expedition(request, climber_id):
    climber = Climber.objects.get(pk=climber_id)

    draft_expedition = get_draft_expedition()

    if draft_expedition is None:
        draft_expedition = Expedition.objects.create()
        draft_expedition.owner = get_current_user()
        draft_expedition.date_created = timezone.now()
        draft_expedition.save()

    if ClimberExpedition.objects.filter(expedition=draft_expedition, climber=climber).exists():
        return redirect("/")

    item = ClimberExpedition(
        expedition=draft_expedition,
        climber=climber
    )
    item.save()

    return redirect("/")


def climber_details(request, climber_id):
    context = {
        "climber": Climber.objects.get(id=climber_id)
    }

    return render(request, "climber_page.html", context)


def delete_expedition(request, expedition_id):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE expeditions SET status = 5 WHERE id = %s", [expedition_id])

    return redirect("/")


def expedition(request, expedition_id):
    context = {
        "expedition": Expedition.objects.get(id=expedition_id),
    }

    return render(request, "expedition_page.html", context)


def get_draft_expedition():
    return Expedition.objects.filter(status=1).first()


def get_current_user():
    return User.objects.filter(is_superuser=False).first()