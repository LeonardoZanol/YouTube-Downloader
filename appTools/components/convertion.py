import os

class Convertions:

    def toMp3(self, file) -> str:
        try:
            base, extension = os.path.splitext(file)
        except:
            return None

        return f"{base}.mp3"

if __name__ == "__main__":
    pass
