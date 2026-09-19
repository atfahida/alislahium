


from django.shortcuts import render, redirect
from .models import Student


def student_list(request):

    students = Student.objects.all()

    return render(
        request,
        "students/student_list.html",
        {
            "students": students
        }
    )


def add_student(request):

    if request.method == "POST":

        student_id = request.POST["student_id"]
        name = request.POST["name"]
        class_name = request.POST["class_name"]
        division = request.POST["division"]
        house = request.POST["house"]
        phone = request.POST["phone"]

        Student.objects.create(
            student_id=student_id,
            name=name,
            class_name=class_name,
            division=division,
            house=house,
            phone=phone
        )

        return redirect("student_list")

    return render(
        request,
        "students/add_student.html"
    )