from django.shortcuts import render, redirect
from .models import Participant
from students.models import Student
from events.models import Event


def participant_list(request):
    participants = Participant.objects.all()

    return render(
        request,
        "participants/participant_list.html",
        {
            "participants": participants
        }
    )


def register_participant(request):
    students = Student.objects.all()
    events = Event.objects.all()

    if request.method == "POST":

        student_id = request.POST.get("student")
        event_id = request.POST.get("event")
        bib_number = request.POST.get("bib_number")

        Participant.objects.create(
            student_id=student_id,
            event_id=event_id,
            bib_number=bib_number
        )

        return redirect("participant_list")

    return render(
        request,
        "participants/register_participant.html",
        {
            "students": students,
            "events": events
        }
    )