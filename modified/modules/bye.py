# For @UniBorg
# Courtesy @yasirsiddiqui

"""
.bye
"""
import time

from telethon.tl.functions.channels import LeaveChannelRequest



@modex.on(modified_cmd("bye"))
@modex.on(sudo_cmd("bye", allow_sudo=True))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        time.sleep(3)
        if e.is_group:
            await e.edit("`This is Very kensur Group, So Me iz Leaving.`")
            await borg(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit("`Boss, This is Not A Chat`")


CMD_HELP.update(
    {
        "bye": "**Bye**\
\n\n**Syntax : **`.bye`\
\n**Usage :** use this plugin to leave a group."
    }
)
