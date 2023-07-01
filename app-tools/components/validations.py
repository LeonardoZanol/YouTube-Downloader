class Validation:

    def url_youtube(self, url: str) -> bool:
        if "https://www.youtube.com/watch?v=" in url or "https://www.youtube.com/shorts/" in url:
            return True
        
        return False