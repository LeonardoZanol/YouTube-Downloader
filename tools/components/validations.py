from .constants import *

from platform import system
from os import path

class Validation:

    def urlYouTube(self, url):
        if VALIDATION_YOUTUBE_VIDEO_URL in url or VALIDATION_YOUTUBE_SHORTS_URL in url:
            return url
        
        return None
    

    def getSystemPathDownload(self):
        home_path = path.expanduser("~")

        if system() == WINDOWS:
            return home_path + WINDOWS_DOWNLOAD_PATH
        
        return home_path + OTHER_SO_DOWNLOAD_PATH
        
    
if __name__ == "__main__":
    pass
    