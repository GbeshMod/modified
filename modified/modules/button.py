"""Create Button Posts
"""

import re

from telethon import custom


BTN_URL_REGEX = re.compile(r"(\{([^\[]+?)\}\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)")


@modex.on(modified_cmd(pattern="cbutton"))  # pylint:disable=E0602
async def _(event):
    if Config.TG_BOT_USER_NAME_BF_HER is None or tgbot is None:
        await event.edit("need to set up a @BotFather bot for this module to work")
        return

    if Config.PRIVATE_CHANNEL_BOT_API_ID is None:
        await event.edit(
            "need to have a `PRIVATE_CHANNEL_BOT_API_ID` for this module to work"
        )
        return

    reply_message = await event.get_reply_message()
    if reply_message is None:
        await event.edit("reply to a message that I need to parse the magic on")
        return

    markdown_note = reply_message.text
    prev = 0
    note_data = ""
    buttons = []
    for match in BTN_URL_REGEX.finditer(markdown_note):
        # Check if btnurl is escaped
        n_escapes = 0
        to_check = match.start(1) - 1
        while to_check > 0 and markdown_note[to_check] == "\\":
            n_escapes += 1
            to_check -= 1

        # if even, not escaped -> create button
        if n_escapes % 2 == 0:
            # create a thruple with button label, url, and newline status
            buttons.append((match.group(2), match.group(3), bool(match.group(4))))
            note_data += markdown_note[prev : match.start(1)]
            prev = match.end(1)

        # if odd, escaped -> move along
        else:
            note_data += markdown_note[prev:to_check]
            prev = match.start(1) - 1

        note_data += markdown_note[prev:]

    message_text = note_data.strip()
    tl_ib_buttons = build_keyboard(buttons)

    tgbot_reply_message = None
    if reply_message.media is not None:
        message_id_in_channel = reply_message.id
        tgbot_reply_message = await tgbot.get_messages(
            entity=Config.PRIVATE_CHANNEL_BOT_API_ID, ids=message_id_in_channel
        )
        tgbot_reply_message = tgbot_reply_message.media

    await tgbot.send_message(
        entity=Config.PRIVATE_CHANNEL_BOT_API_ID,
        message=message_text,
        parse_mode="html",
        file=tgbot_reply_message,
        link_preview=False,
        buttons=tl_ib_buttons,
        silent=True,
    )


def build_keyboard(buttons):
    keyb = []
    for btn in buttons:
        if btn[2] and keyb:
            keyb[-1].append(custom.Button.url(btn[0], btn[1]))
        else:
            keyb.append([custom.Button.url(btn[0], btn[1])])
    return keyb



@bot.on(admin_cmd(pattern=r"ibutton( (.*)|$)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"ibutton( (.*)|$)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_to_id = None
    catinput = "".join(event.text.split(maxsplit=1)[1:])
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    await event.get_reply_message()
    # soon will try to add media support
    if not catinput:
        catinput = (await event.get_reply_message()).text
    if not catinput:
        await edit_or_reply(event, "`Give me something to write in bot inline`")
        return
    catinput = "Inline buttons " + catinput
    tgbotusername = Config.TG_BOT_USER_NAME_BF_HER
    results = await bot.inline_query(tgbotusername, catinput)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


def build_keyboard(buttons):
    keyb = []
    for btn in buttons:
        if btn[2] and keyb:
            keyb[-1].append(Button.url(btn[0], btn[1]))
        else:
            keyb.append([Button.url(btn[0], btn[1])])
    return keyb


CMD_HELP.update(
    {
        "button": f"**Plugin : **`button`\
    \n\n**Button post helper**\
    \n  •  **Syntax : **`.cbutton`\
    \n  •  **Usage :** __For working of this you need your bot({BOT_USERNAME}) in the group/channel you are using and Buttons must be in the format as [Name on button]<buttonurl:link you want to open> and markdown is Default to html__\
    \n  •  **Example :** `.cbutton test [google]<buttonurl:https://www.google.com> [catuserbot]<buttonurl:https://t.me/catuserbot17:same> [support]<buttonurl:https://t.me/catuserbot_support>`\
    \n\n  •  **Syntax : **`.ibutton`\
    \n  •  **Function :** __Buttons must be in the format as [Name on button]<buttonurl:link you want to open>__\
    \n  •  **Example :** `.ibutton test [google]<buttonurl:https://www.google.com> [catuserbot]<buttonurl:https://t.me/catuserbot17:same> [support]<buttonurl:https://t.me/catuserbot_support>`\
    "
    }
)
