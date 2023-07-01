import flet as ft

from components.youtube_download import *
from components.validations import *

from constants import *

def main(page: ft.Page):
    page.title = TITLE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def download(e):
        url = box_text.value
        box_text.error_text = None

        if Validation().url_youtube(url):
            button_download.disabled = True
            button_clear.disabled = True

            control_progress_ring = ft.Row(
                [ft.ProgressRing()]
                , alignment = ft.MainAxisAlignment.CENTER
            )

            page.add(control_progress_ring)

            if Download().download_audio(url):
                page.controls.remove(control_progress_ring)

        else:
            box_text.error_text = "[ Error ] - URL Not Found!"
    
        page.update()


    def clear(e):
       
       # Clear Box Text - Add Focus in the Box.

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
