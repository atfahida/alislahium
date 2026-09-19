from django.shortcuts import render, redirect
from .models import Event, Category


def event_list(request):

    events = Event.objects.all()

    return render(
        request,
        "events/event_list.html",
        {
            "events": events
        }
    )


def add_event(request):

    categories = Category.objects.all()

    if request.method == "POST":

        event_name = request.POST["event_name"]
        category_id = request.POST["category"]
        event_type = request.POST["event_type"]
        stage = request.POST["stage"]

        Event.objects.create(
            event_name=event_name,
            category_id=category_id,
            event_type=event_type,
            stage=stage
        )

        return redirect("event_list")

    return render(
        request,
        "events/add_event.html",
        {
            "categories": categories
        }
    )