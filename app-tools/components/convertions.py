import os

class Extensions:

    def mp3(self, file) -> bool:
        try:
            base, ext = os.path.splitext()
            os.rename(file, base + ".mp3")

        except:
            return False
        
        return True
    