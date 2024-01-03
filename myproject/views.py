from django.shortcuts import render


def view1(request):
    return render(request, "template1.html", {"a": 1})
