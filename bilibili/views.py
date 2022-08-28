from django.http import HttpResponse
from django.shortcuts import render
import datetime


def index(request):
    return render(request, "yt-dlp.html")


def down(request):
    url = request.POST.get("url")
    if url == "":
        return HttpResponse("hello youtubedl")
    else:
        down_video(url)
        return HttpResponse("down successful")


from yt_dlp import YoutubeDL


def down_video(url):
    # path
    # path = "/home/chaoge/test/"
    # cloudpath
    path = "/home/data/"

    # URLS = [url]

    time = str(datetime.datetime.now())
    ydl_opts = {
        'outtmpl': path + time + '.%(ext)s',
        'noplaylist': True
    }
    with YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(
            url,  # 视频链接
            download=True,  # 不下载只是抽取信息
        )
