from pytube import YouTube

import flet as ft

from . components.validations import *
from . components.convertion  import *
from . components.constants   import *

path = Validation().getSystemPathDownload()

class Message:

    def generate(self, title="", content="", actions=[], openMessage=False):
        return ft.AlertDialog(
            open              = openMessage,
            modal             = True,
            title             = ft.Text(title, text_align=ft.TextAlign.CENTER),
            content           = ft.Text(content, text_align=ft.TextAlign.CENTER),
            actions           = actions,
            actions_alignment = ft.MainAxisAlignment.CENTER
        )


def downlaod(url, type):
    try:
        objectYouTubeDownlaod = YouTube(Validation().urlYouTube(url)).streams
        if type == RADIO_VALUE_VIDEO:
            objectYouTubeDownlaod.get_highest_resolution().download(output_path=path)
        else:
            objectYouTubeDownlaod.get_audio_only().download(output_path=path)

    except:
        return False
   
    return True
        

def main(page: ft.Page):    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_center()
    page.title = TITLE

    def constructMessageStatusDownload(title="", content="", actions=[]):
        messageStatusDownlaod.title             = ft.Text(title, text_align=ft.TextAlign.CENTER)
        messageStatusDownlaod.content           = ft.Text(content, text_align=ft.TextAlign.CENTER)
        messageStatusDownlaod.actions           = actions
        messageStatusDownlaod.actions_alignment = ft.MainAxisAlignment.CENTER

        page.update()


    def submitDownload(e):
        inputBoxUrl.error_text = None
        inputBoxUrl.focus()

        if not radioGroupTypeObject.value or not inputBoxUrl.value:
            inputBoxUrl.error_text = DATA_INVALID_INFORMATION

        elif not Validation().urlYouTube(inputBoxUrl.value):
            messageErrorUrlInvalid.open = True
            page.dialog = messageErrorUrlInvalid

        else:
            

            messageStatusDownlaod.open = True
            page.dialog = messageStatusDownlaod

            constructMessageStatusDownload(MESSAGE_TITLE_DQWNLOAD_PROCESSING, MESSAGE_CONTENT_DOWNLOAD_PROCESSING, actions=[ft.ProgressRing()])

            if not downlaod(inputBoxUrl.value, radioGroupTypeObject.value):
                constructMessageStatusDownload(MESSAGE_TITLE_ALERT_DOWNLOAD_NOT_CONFIRMED, MESSAGE_CONTENT_ALERT_DOWNLOAD_NOT_CONFIRMED, actions)

            else:
                constructMessageStatusDownload(MESSAGE_TITLE_ALERT_DOWNLOAD_CONFIRMED, MESSAGE_CONTENT_ALERT_DOWNLOAD_CONFIRMED, actions)
                
                inputBoxUrl.value          = None
                radioGroupTypeObject.value = None

        page.update()


    def destroy_aplication(e):
        page.window_destroy()


    def exitAplication(e):
        messageCloseAplication.open = True
        page.dialog = messageCloseAplication

        page.update()


    def closeMessage(e):
        page.dialog.open = False
        page.update()


    def validateKeyboardEvent(e: ft.KeyboardEvent):
        if e.key == ENTER_KEY:
            submitDownload(e)


    actions = [
        ft.IconButton(ft.icons.CLOSE, on_click=closeMessage)
    ]

    actionsCloseAplication = [
        ft.ElevatedButton(MESSAGE_BUTTON_CONFIRM, on_click=destroy_aplication),
        ft.ElevatedButton(MESSAGE_BUTTON_NO_CONFIRM, on_click=closeMessage)
    ]

    messageTitle = ft.Text(TITLE, text_align=ft.TextAlign.CENTER, size=50)
    inputBoxUrl  = ft.TextField(hint_text=HINT_TEXT_INPUT_BOX, width=500, text_align=ft.TextAlign.CENTER)
    
    radioGroupTypeObject = ft.RadioGroup(content=ft.Row([
        ft.Radio(value=RADIO_VALUE_VIDEO, label=RADIO_LABEL_VIDEO),
        ft.Radio(value=RADIO_VALUE_AUDIO, label=RADIO_LABEL_AUDIO)
    ]))

    buttonSubmitDownload = ft.ElevatedButton(BUTTON_DOWNLOAD, on_click=submitDownload)
    buttonExit           = ft.ElevatedButton(BUTTON_EXIT, width=120, on_click=exitAplication)

    messageCloseAplication           = Message().generate(MESSAGE_ALERT_EXIT_TITLE, MESSAGE_ALERT_EXIT_CONTENT, actionsCloseAplication, True)
    messageErrorUrlInvalid           = Message().generate(MESSAGE_TITLE_ALERT_INVALID_URL, MESSAGE_CONTENT_ALERT_INVALID_URL, actions)

    messageStatusDownlaod            = ft.AlertDialog(
        modal = True
    )

    page.on_keyboard_event = validateKeyboardEvent

    page.add(
        ft.Row(
            [messageTitle], 
            alignment=ft.MainAxisAlignment.CENTER
        ),

        ft.Row(
            [inputBoxUrl], 
            alignment=ft.MainAxisAlignment.CENTER
        ),

        ft.Row(
            [radioGroupTypeObject], 
            alignment=ft.MainAxisAlignment.CENTER
        ),

        ft.Row(
            [buttonSubmitDownload, buttonExit], 
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
