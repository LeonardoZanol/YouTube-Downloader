import flet as ft

from constants import *
from components.youtube_download import *

def main(page: ft.Page):
    page.title = TITLE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def download(e):
        url = box_text.value
        box_text.error_text = None
        box_text.focus()

        if "https://www.youtube.com/watch?v=" in url or "https://www.youtube.com/shorts/" in url:
            pass

        else:
            box_text.error_text = "Please enter a valid URL"

        page.update()
        

    def clear(e):
       box_text.value = ""
       box_text.focus()

       page.update()


    box_text = ft.TextField(hint_text= "Enter The Desired URL Here", value="", width=400, text_align=ft.TextAlign.LEFT, autofocus=True)

    button_download = ft.IconButton(ft.icons.DOWNLOAD, on_click=download)
    button_clear = ft.IconButton(ft.icons.CLEAR, on_click=clear)

    page.add(
        ft.Row(
            [button_clear, box_text, button_download],
            alignment = ft.MainAxisAlignment.CENTER
        )
    )


ft.app(target=main)
