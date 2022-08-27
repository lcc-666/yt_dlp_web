from django.http import HttpResponse
from django.shortcuts import render
import os


def index(request):
    return render(request, "yt-dlp.html")


def down(request):
    url=request.POST.get("url")
    if url == "":
        return HttpResponse("hello youtubedl")
    else:
        os.system("source /home/environment/my_django/bin/activate ;"
                  "cd /home/yt_dlp_web/bilibili/ ; mkdir ./5554")
        return HttpResponse("down successful")

