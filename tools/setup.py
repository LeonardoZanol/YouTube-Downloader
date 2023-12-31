import flet as ft

from . components.validations import *
from . components.constants   import *

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
        

def main(page: ft.Page):    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_center()
    page.title = f"{TITLE} + {VERSION}"

    def submeteDownload(e):
        inputBoxUrl.error_text = None
        inputBoxUrl.focus()

        if not radioGroupTypeObject.value or not inputBoxUrl.value:
            inputBoxUrl.error_text = DATA_INVALID_INFORMATION

        elif not Validation().urlYouTube(inputBoxUrl.value):
            messageErrorUrlInvalid.open = True
            page.dialog = messageErrorUrlInvalid

        else:
            messageDownloadProcessing.open = True
            page.dialog = messageDownloadProcessing
            page.update()

            if not Validation().downloadYoutube(inputBoxUrl.value, radioGroupTypeObject.value):
                messageDownloadNotConfirm.open = True
                page.dialog = messageDownloadNotConfirm
                page.update()

            else:
                messageDownloadConfirm.open = True
                page.dialog = messageDownloadConfirm

                radioGroupTypeObject.value = None
                inputBoxUrl.value = None
                page.update()

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

    buttonSubmitDownload = ft.ElevatedButton(BUTTON_DOWNLOAD, on_click=submeteDownload)
    buttonExit           = ft.ElevatedButton(BUTTON_EXIT, width=120, on_click=exitAplication)

    messageCloseAplication = Message().generate(MESSAGE_ALERT_EXIT_TITLE, MESSAGE_ALERT_EXIT_CONTENT, actionsCloseAplication, True)
    messageErrorUrlInvalid = Message().generate(MESSAGE_TITLE_ALERT_INVALID_URL, MESSAGE_CONTENT_ALERT_INVALID_URL, actions)

    messageDownloadNotConfirm = Message().generate(MESSAGE_TITLE_ALERT_DOWNLOAD_NOT_CONFIRMED, MESSAGE_CONTENT_ALERT_DOWNLOAD_NOT_CONFIRMED, actions)
    messageDownloadProcessing = Message().generate(MESSAGE_TITLE_DQWNLOAD_PROCESSING, MESSAGE_CONTENT_DOWNLOAD_PROCESSING, [ft.ProgressRing()])
    messageDownloadConfirm = Message().generate(MESSAGE_TITLE_ALERT_DOWNLOAD_CONFIRMED, MESSAGE_CONTENT_ALERT_DOWNLOAD_CONFIRMED, actions)

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
