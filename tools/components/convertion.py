import os

from os.path import splitext

class Convertions:

    def __init__(self) -> None:
        self.__mp3 = ".mp3"

    def toMp3(self, file_path:str) -> bool:
        try:
            base, ext = splitext(file_path)
            os.rename(file_path, base + self.__mp3)
        except:
            return False
        
        return True
    
if __name__ == "__main__":
    pass