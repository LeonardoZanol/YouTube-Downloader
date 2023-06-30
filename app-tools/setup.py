import flet as ft

from constants import *
from components.youtube_download import *

def main(page: ft.Page):
    page.title = TITLE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def download(e):
        pass
        

    def clear(e):
       box_text.value = ""
       button_clear.focus()

       page.update()


    box_text = ft.TextField(hint_text= "Enter The Desired URL Here", value="", width=400, text_align=ft.TextAlign.LEFT, autofocus=True)

    button_download = ft.IconButton(ft.icons.DOWNLOAD, on_click=download)
    button_clear = ft.IconButton(ft.icons.CLEAR, on_click=clear)

    check_box = ft.RadioGroup(content = ft.Row([
        ft.Radio(value="Audio", label="Audio"),
        ft.Radio(value="Video", label="Video")
    ]))

    page.add(
        ft.Row(
            [button_clear, box_text, button_download],
            alignment = ft.MainAxisAlignment.CENTER
        ),

        ft.Row([check_box], alignment = ft.MainAxisAlignment.CENTER)
    )


ft.app(target=main)
