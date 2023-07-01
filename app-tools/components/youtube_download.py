from typing import Optional

from pytube import YouTube as Yt
from os import environ

from convertions import *

class Download:

    def __init__(self, path_download: Optional[str]=None) -> None:
        self.path_download = environ["HOMEPATH"] + "/Downloads/YouTubeDownloader/"


    def download_audio(self, url: str) -> bool:
        try:
            object = Yt(url).streams.get_audio_only().download(output_path=self.path_download)
        except:
            return False  
        else:
            if Extensions.mp3(object):
                return True
            

if __name__ == "__main__":
    pass
        