from yt_dlp import YoutubeDL


def down_video(url):
    # path
    #path = "/home/chaoge/test/"
    # cloudpath
    path = "/home/data/"
    URLS = [url]

    ydl_opts = {
        'noplaylist': True,
        "outtmpl": path + '%(title)s.%(ext)s'
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(URLS)


if __name__ == '__main__':
    # URL="https://cn.pornhub.com/view_video.php?viewkey=ph63026168399b0"
    word=input()
    URL = word
    down_video(URL)
