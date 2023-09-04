import os

class Convertions:

    def toMp3(self, file):
        try:
            base, ext = os.path.splitext(file)
        
        except:
            return False
        
        os.rename(file, f"{base}.mp3")

