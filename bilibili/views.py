from django.http import HttpResponse
from django.shortcuts import render
import shutil


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
    path = "/home/chaoge/test/"
    # cloudpath
    # path = "/home/data/"

    #URLS = [url]

    ydl_opts = {
        'outtmpl': path + '%(title)s.%(ext)s',
        'noplaylist': True
    }
    with YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(
            url,  # 视频链接
            download=True,  # 不下载只是抽取信息
        )
    title = result["title"]
    old = "/home/data/_.mp4"
    new = "/home/data/%s.mp4" % title
    shutil.move(old, new)
