from django.shortcuts import render, redirect
from .models import Result
from participants.models import Participant


def result_list(request):

    results = Result.objects.all()

    return render(
        request,
        "results/result_list.html",
        {
            "results": results
        }
    )


def add_result(request):

    participants = Participant.objects.all()

    if request.method == "POST":

        participant_id = request.POST["participant"]
        place = request.POST["place"]
        grade = request.POST["grade"]

        Result.objects.create(
            participant_id=participant_id,
            place=place,
            grade=grade
        )

        return redirect("result_list")

    return render(
        request,
        "results/add_result.html",
        {
            "participants": participants
        }
    )