from django.shortcuts import render
import time


def view1(request):
    return render(request, "template1.html", {"a": 1})


def view2(request, seconds=0):
    if seconds:
        time.sleep(seconds)
    else:
        seconds = 3
        time.sleep(seconds)

    return render(request, "template2.html", {"seconds": seconds})
