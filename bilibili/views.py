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
        cmd="/home/environment/my_django/bin/python youtube.py %s"%url
        os.system(cmd)
        return HttpResponse("down successful")

