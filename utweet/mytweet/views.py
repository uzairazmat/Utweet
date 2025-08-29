from django.shortcuts import render

# Create your views here.


def mytweet(request):
    return render(request, "websites/mytweet.html")
