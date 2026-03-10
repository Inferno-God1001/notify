import os

def send(
    title=None,
    content=None,
    id=None,
    priority=None,
    sound=None,
    vibrate=None,
    ongoing=None,
    button1=None,
    button1_action=None,
    button2=None,
    button2_action=None,
    button3=None,
    button3_action=None,
    icon=None
):

    cmd = "termux-notification"

    if title:
        cmd += f' --title "{title}"'

    if content:
        cmd += f' --content "{content}"'

    if id:
        cmd += f' --id {id}'

    if priority:
        cmd += f' --priority {priority}'

    if sound:
        cmd += f' --sound'

    if vibrate:
        cmd += f' --vibrate'

    if ongoing:
        cmd += f' --ongoing'

    if button1:
        cmd += f' --button1 "{button1}"'

    if button1_action:
        cmd += f' --button1-action "{button1_action}"'

    if button2:
        cmd += f' --button2 "{button2}"'

    if button2_action:
        cmd += f' --button2-action "{button2_action}"'

    if button3:
        cmd += f' --button3 "{button3}"'

    if button3_action:
        cmd += f' --button3-action "{button3_action}"'

    if icon:
        cmd += f' --icon "{icon}"'

    os.system(cmd)
