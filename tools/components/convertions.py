import os

class Convertion:

    def __init__(self, file_path:str) -> None:
        self.__file_path = file_path
        self.__mp3 = ".mp3"


    def toMp3(self) -> bool:
        try:
            base, ext = os.path.splitext(self.__file_path)
            os.rename(self.__file_path, base + self.__mp3)
        except:
            return False
        return True
    