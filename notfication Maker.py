from plyer import notification
def notification_creater(headline,messages):
    notification.notify(
        title=headline,
        message=messages,
        timeout=5
    )
notification_creater("MyComputer", "PAPUTU")    