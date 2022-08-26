from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "yt-dlp.html")


def down(request):
    url=request.POST.get("url")
    if url is "":
        return HttpResponse("hello youtubedl")
    else:
        down_video(url)
        return HttpResponse("down successful")


from yt_dlp import YoutubeDL


def down_video(url):
    path = "/home/chaoge/test/"
    URLS=[url]

    ydl_opts={
        'noplaylist': True,
        "outtmpl": path + '%(title)s.%(ext)s'
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(URLS)