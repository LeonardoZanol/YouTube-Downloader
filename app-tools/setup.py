from pytube import YouTube
import flet as ft
import os

import constants as c

path = os.environ["HOME"] + "/Downloads/YouTubeDownloader"

class Message:

    def generate(self, title, content, actions, openMessage=False):
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
        objectYouTubeDownlaod = YouTube(url).streams
        if type == c.RADIO_VALUE_VIDEO:
            objectYouTubeDownlaod.get_highest_resolution().download(output_path=path)
        else:
            objectYouTubeDownlaod.get_audio_only().download(output_path=path)
    except:
        return False
    else:
        return True


def validateUrl(url):
    if c.VALIDATION_YOUTUBE_VIDEO_URL in url or c.VALIDATION_YOUTUBE_SHORTS_URL in url:
        return True
    
    return False
        

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.title = c.TITLE

    def submeteDownload(e):
        inputBoxUrl.error_text = ""
        inputBoxUrl.focus()

        if not radioGroupTypeObject.value or not inputBoxUrl.value:
            inputBoxUrl.error_text = c.DATA_INVALID_INFORMATION

        elif not validateUrl(inputBoxUrl.value):
            messageErrorUrlInvalid.open = True
            page.dialog = messageErrorUrlInvalid

        else:
            if not downlaod(inputBoxUrl.value, radioGroupTypeObject.value):
                messageErrorDownloadNotConfirmed.open = True
                page.dialog = messageErrorDownloadNotConfirmed

            else:
                messageDownloadConfirmed.open = True
                page.dialog = messageDownloadConfirmed
            
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
        if e.key == c.ENTER_KEY:
            submeteDownload(e)


    actions = [
        ft.IconButton(ft.icons.CLOSE, on_click=closeMessage)
    ]

    actionsCloseAplication = [
        ft.ElevatedButton(c.MESSAGE_BUTTON_CONFIRM, on_click=destroy_aplication),
        ft.ElevatedButton(c.MESSAGE_BUTTON_NO_CONFIRM, on_click=closeMessage)
    ]

    messageTitle = ft.Text(c.TITLE, text_align=ft.TextAlign.CENTER, size=50)
    inputBoxUrl  = ft.TextField(hint_text=c.HINT_TEXT_INPUT_BOX, width=430, text_align=ft.TextAlign.CENTER)
    
    radioGroupTypeObject = ft.RadioGroup(content=ft.Row([
        ft.Radio(value=c.RADIO_VALUE_VIDEO, label=c.RADIO_LABEL_VIDEO),
        ft.Radio(value=c.RADIO_VALUE_AUDIO, label=c.RADIO_LABEL_AUDIO)
    ]))

    buttonSubmitDownload = ft.ElevatedButton(c.BUTTON_DOWNLOAD, on_click=submeteDownload)
    buttonExit           = ft.ElevatedButton(c.BUTTON_EXIT, width=120, on_click=exitAplication)

    messageCloseAplication           = Message().generate(c.MESSAGE_ALERT_EXIT_TITLE, c.MESSAGE_ALERT_EXIT_CONTENT, actionsCloseAplication, True)
    messageErrorUrlInvalid           = Message().generate(c.MESSAGE_TITLE_ALERT_INVALID_URL, c.MESSAGE_CONTENT_ALERT_INVALID_URL, actions)
    messageErrorDownloadNotConfirmed = Message().generate(c.MESSAGE_TITLE_ALERT_DOWNLOAD_NOT_CONFIRMED, c.MESSAGE_CONTENT_ALERT_DOWNLOAD_NOT_CONFIRMED, actions)
    messageDownloadConfirmed         = Message().generate(c.MESSAGE_TITLE_ALERT_DOWNLOAD_CONFIRMED, c.MESSAGE_CONTENT_ALERT_DOWNLOAD_CONFIRMED, actions)

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


ft.app(target=main)
