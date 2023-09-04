from .constants import *
import os

class Validation:

    def urlYouTube(self, url):
        if VALIDATION_YOUTUBE_VIDEO_URL in url or VALIDATION_YOUTUBE_SHORTS_URL in url:
            return url
        
        return None
    

    def getSystemPathDownload(self):
        environ = os.environ
        
        if WINDOWS in environ[DESKTOP_SESSION]:
            return  environ[WINDOWS_ENVIRON] + WINDOWS_DOWNLOAD_PATH
        
        return environ[OTHER_SO_ENVIRON] + OTHER_SO_DOWNLOAD_PATH

    
if __name__ == "__main__":
    pass
    