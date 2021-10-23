import pytube
import youtube_dl
import time
import os

class Video():
    def __init__(self, url, name, res="360"):
        self.url=url
        self.res=int(res)
        self.name=name

    async def download(self):
        video=pytube.YouTube(self.url)
        #try:
            #res=360 is 18
            #res=720 is 22
            #res=1080 is 137
        match self.res:
            case 360:
                stream=video.streams.get_by_itag(18)
            case 720:
                stream=video.streams.get_by_itag(22)
            case 1080:
                stream=video.streams.get_by_itag(137)
        stream.download(filename=self.name)
        #except:
        #    opts={"outtmpl":self.name}
        #    with youtube_dl.YoutubeDL(opts) as ydl:
        #        ydl.download([self.url]) 
    
    async def remove(self):
            os.remove(self.name)
            return        